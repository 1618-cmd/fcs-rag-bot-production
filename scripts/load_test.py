#!/usr/bin/env python3
"""
Load Testing Script for FCS RAG Bot
Simulates concurrent users to test system robustness.

Usage:
    python scripts/load_test.py --users 50 --duration 60 --endpoint query
    python scripts/load_test.py --users 50 --duration 60 --scenario mixed
    python scripts/load_test.py --users 100 --duration 120 --scenario peak
"""

import asyncio
import aiohttp
import time
import argparse
import json
import statistics
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Sample test data
SAMPLE_QUESTIONS = [
    "How do I configure Line Item Details in Vena?",
    "What is the difference between VenaQL and Vena Copilot?",
    "How do I troubleshoot a VenaQL script that returns no values?",
    "What are the best practices for Vena data modeling?",
    "How do I set up workflows in Vena?",
    "What is the syntax for VenaQL calculation scripts?",
    "How do I configure Assumed Members?",
    "What are the limitations of VenaQL?",
    "How do I use Scope statements in VenaQL?",
    "What is the difference between Input Tasks and Calculation Scripts?",
]

SAMPLE_CALC_SCRIPT = """Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}
@source1 = [Account.7300].Sum()
Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}
@this = @source1"""


@dataclass
class RequestResult:
    """Result of a single HTTP request."""
    endpoint: str
    status_code: int
    response_time_ms: float
    success: bool
    error: Optional[str] = None
    timestamp: float = 0.0


@dataclass
class LoadTestMetrics:
    """Aggregated metrics from load test."""
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    avg_response_time_ms: float
    min_response_time_ms: float
    max_response_time_ms: float
    p50_response_time_ms: float
    p95_response_time_ms: float
    p99_response_time_ms: float
    requests_per_second: float
    error_breakdown: Dict[str, int]
    endpoint: str


class LoadTester:
    """Load testing client using asyncio."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.results: List[RequestResult] = []
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def make_query_request(self, question: str) -> RequestResult:
        """Make a query request to /api/query."""
        start_time = time.time()
        try:
            async with self.session.post(
                f"{self.base_url}/api/query",
                json={"question": question},
                headers={"Content-Type": "application/json"}
            ) as response:
                response_time = (time.time() - start_time) * 1000
                text = await response.text()
                
                return RequestResult(
                    endpoint="query",
                    status_code=response.status,
                    response_time_ms=response_time,
                    success=response.status == 200,
                    error=None if response.status == 200 else f"HTTP {response.status}: {text[:100]}",
                    timestamp=start_time
                )
        except asyncio.TimeoutError:
            return RequestResult(
                endpoint="query",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error="Timeout",
                timestamp=start_time
            )
        except Exception as e:
            return RequestResult(
                endpoint="query",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error=str(e)[:100],
                timestamp=start_time
            )
    
    async def make_calc_script_request(self, question: str, calc_script: str) -> RequestResult:
        """Make a calc script analysis request."""
        start_time = time.time()
        try:
            async with self.session.post(
                f"{self.base_url}/api/query",
                json={
                    "question": question,
                    "calc_script": calc_script
                },
                headers={"Content-Type": "application/json"}
            ) as response:
                response_time = (time.time() - start_time) * 1000
                text = await response.text()
                
                return RequestResult(
                    endpoint="calc_script",
                    status_code=response.status,
                    response_time_ms=response_time,
                    success=response.status == 200,
                    error=None if response.status == 200 else f"HTTP {response.status}: {text[:100]}",
                    timestamp=start_time
                )
        except asyncio.TimeoutError:
            return RequestResult(
                endpoint="calc_script",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error="Timeout",
                timestamp=start_time
            )
        except Exception as e:
            return RequestResult(
                endpoint="calc_script",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error=str(e)[:100],
                timestamp=start_time
            )
    
    async def make_login_request(self, email: str, password: str) -> RequestResult:
        """Make a login request."""
        start_time = time.time()
        try:
            async with self.session.post(
                f"{self.base_url}/api/auth/login",
                json={"email": email, "password": password},
                headers={"Content-Type": "application/json"}
            ) as response:
                response_time = (time.time() - start_time) * 1000
                text = await response.text()
                
                return RequestResult(
                    endpoint="login",
                    status_code=response.status,
                    response_time_ms=response_time,
                    success=response.status == 200,
                    error=None if response.status == 200 else f"HTTP {response.status}: {text[:100]}",
                    timestamp=start_time
                )
        except asyncio.TimeoutError:
            return RequestResult(
                endpoint="login",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error="Timeout",
                timestamp=start_time
            )
        except Exception as e:
            return RequestResult(
                endpoint="login",
                status_code=0,
                response_time_ms=(time.time() - start_time) * 1000,
                success=False,
                error=str(e)[:100],
                timestamp=start_time
            )
    
    async def simulate_user(self, user_id: int, scenario: str, duration: float) -> List[RequestResult]:
        """Simulate a single user making requests."""
        user_results = []
        start_time = time.time()
        request_count = 0
        
        while time.time() - start_time < duration:
            if scenario == "query":
                question = SAMPLE_QUESTIONS[request_count % len(SAMPLE_QUESTIONS)]
                result = await self.make_query_request(question)
                user_results.append(result)
            
            elif scenario == "calc_script":
                question = "What is this script doing? Why isn't it returning values?"
                result = await self.make_calc_script_request(question, SAMPLE_CALC_SCRIPT)
                user_results.append(result)
            
            elif scenario == "login":
                result = await self.make_login_request("admin@example.com", "admin")
                user_results.append(result)
            
            elif scenario == "mixed":
                # Mix of different request types
                request_type = request_count % 3
                if request_type == 0:
                    question = SAMPLE_QUESTIONS[request_count % len(SAMPLE_QUESTIONS)]
                    result = await self.make_query_request(question)
                elif request_type == 1:
                    question = "What is this script doing?"
                    result = await self.make_calc_script_request(question, SAMPLE_CALC_SCRIPT)
                else:
                    result = await self.make_login_request("admin@example.com", "admin")
                user_results.append(result)
            
            request_count += 1
            
            # Small delay between requests (simulate thinking time)
            await asyncio.sleep(0.5)
        
        return user_results
    
    async def run_load_test(
        self,
        num_users: int,
        duration: float,
        scenario: str = "query"
    ) -> List[RequestResult]:
        """Run load test with specified number of concurrent users."""
        print(f"\n🚀 Starting load test:")
        print(f"   Users: {num_users}")
        print(f"   Duration: {duration}s")
        print(f"   Scenario: {scenario}")
        print(f"   Target: {self.base_url}\n")
        
        # Create tasks for all users
        tasks = [
            self.simulate_user(user_id, scenario, duration)
            for user_id in range(num_users)
        ]
        
        # Run all users concurrently
        start_time = time.time()
        all_results = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        
        # Flatten results and handle exceptions
        results = []
        for user_results in all_results:
            if isinstance(user_results, Exception):
                print(f"⚠️  User task failed: {user_results}")
            else:
                results.extend(user_results)
        
        actual_duration = end_time - start_time
        print(f"\n✅ Load test completed in {actual_duration:.2f}s")
        print(f"   Total requests: {len(results)}\n")
        
        return results
    
    def calculate_metrics(self, results: List[RequestResult], endpoint: str = "all") -> LoadTestMetrics:
        """Calculate aggregated metrics from results."""
        if endpoint != "all":
            results = [r for r in results if r.endpoint == endpoint]
        
        if not results:
            return LoadTestMetrics(
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                avg_response_time_ms=0.0,
                min_response_time_ms=0.0,
                max_response_time_ms=0.0,
                p50_response_time_ms=0.0,
                p95_response_time_ms=0.0,
                p99_response_time_ms=0.0,
                requests_per_second=0.0,
                error_breakdown={},
                endpoint=endpoint
            )
        
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        response_times = [r.response_time_ms for r in results]
        response_times_sorted = sorted(response_times)
        
        # Calculate percentiles
        def percentile(data, p):
            if not data:
                return 0.0
            k = (len(data) - 1) * p
            f = int(k)
            c = k - f
            if f + 1 < len(data):
                return data[f] + c * (data[f + 1] - data[f])
            return data[f]
        
        # Error breakdown
        error_breakdown = {}
        for r in failed:
            error_key = r.error or f"HTTP {r.status_code}"
            error_breakdown[error_key] = error_breakdown.get(error_key, 0) + 1
        
        # Calculate duration
        if results:
            duration = max(r.timestamp for r in results) - min(r.timestamp for r in results)
            if duration == 0:
                duration = 1.0
        else:
            duration = 1.0
        
        return LoadTestMetrics(
            total_requests=len(results),
            successful_requests=len(successful),
            failed_requests=len(failed),
            success_rate=(len(successful) / len(results)) * 100 if results else 0.0,
            avg_response_time_ms=statistics.mean(response_times) if response_times else 0.0,
            min_response_time_ms=min(response_times) if response_times else 0.0,
            max_response_time_ms=max(response_times) if response_times else 0.0,
            p50_response_time_ms=percentile(response_times_sorted, 0.50),
            p95_response_time_ms=percentile(response_times_sorted, 0.95),
            p99_response_time_ms=percentile(response_times_sorted, 0.99),
            requests_per_second=len(results) / duration if duration > 0 else 0.0,
            error_breakdown=error_breakdown,
            endpoint=endpoint
        )
    
    def print_metrics(self, metrics: LoadTestMetrics):
        """Print formatted metrics."""
        print(f"\n{'='*60}")
        print(f"📊 LOAD TEST RESULTS - {metrics.endpoint.upper()}")
        print(f"{'='*60}\n")
        
        print(f"Total Requests:      {metrics.total_requests:,}")
        print(f"Successful:           {metrics.successful_requests:,}")
        print(f"Failed:               {metrics.failed_requests:,}")
        print(f"Success Rate:         {metrics.success_rate:.2f}%\n")
        
        print(f"Response Times:")
        print(f"  Average:            {metrics.avg_response_time_ms:.2f} ms")
        print(f"  Min:                {metrics.min_response_time_ms:.2f} ms")
        print(f"  Max:                {metrics.max_response_time_ms:.2f} ms")
        print(f"  P50 (Median):       {metrics.p50_response_time_ms:.2f} ms")
        print(f"  P95:                {metrics.p95_response_time_ms:.2f} ms")
        print(f"  P99:                {metrics.p99_response_time_ms:.2f} ms\n")
        
        print(f"Throughput:           {metrics.requests_per_second:.2f} req/s\n")
        
        if metrics.error_breakdown:
            print(f"Error Breakdown:")
            for error, count in sorted(metrics.error_breakdown.items(), key=lambda x: x[1], reverse=True):
                print(f"  {error}: {count}")
            print()
        
        print(f"{'='*60}\n")
    
    def save_report(self, metrics: LoadTestMetrics, filename: Optional[str] = None):
        """Save metrics to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"load_test_report_{timestamp}.json"
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "metrics": asdict(metrics)
        }
        
        report_path = project_root / "scripts" / filename
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Report saved to: {report_path}\n")


async def main():
    parser = argparse.ArgumentParser(description="Load test FCS RAG Bot API")
    parser.add_argument(
        "--url",
        type=str,
        default="http://localhost:8000",
        help="Base URL of the API (default: http://localhost:8000)"
    )
    parser.add_argument(
        "--users",
        type=int,
        default=50,
        help="Number of concurrent users (default: 50)"
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=60,
        help="Test duration in seconds (default: 60)"
    )
    parser.add_argument(
        "--scenario",
        type=str,
        choices=["query", "calc_script", "login", "mixed"],
        default="mixed",
        help="Test scenario (default: mixed)"
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        choices=["query", "calc_script", "login", "all"],
        default="all",
        help="Endpoint to test (default: all)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: 30)"
    )
    parser.add_argument(
        "--save-report",
        action="store_true",
        help="Save results to JSON file"
    )
    
    args = parser.parse_args()
    
    async with LoadTester(args.url, timeout=args.timeout) as tester:
        # Run load test
        results = await tester.run_load_test(
            num_users=args.users,
            duration=args.duration,
            scenario=args.scenario
        )
        
        # Calculate and print metrics
        if args.endpoint == "all":
            # Print metrics for each endpoint type
            endpoints = ["query", "calc_script", "login"]
            for endpoint in endpoints:
                endpoint_results = [r for r in results if r.endpoint == endpoint]
                if endpoint_results:
                    metrics = tester.calculate_metrics(results, endpoint)
                    tester.print_metrics(metrics)
            
            # Print overall metrics
            overall_metrics = tester.calculate_metrics(results, "all")
            tester.print_metrics(overall_metrics)
            
            if args.save_report:
                tester.save_report(overall_metrics)
        else:
            metrics = tester.calculate_metrics(results, args.endpoint)
            tester.print_metrics(metrics)
            
            if args.save_report:
                tester.save_report(metrics)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Load test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
