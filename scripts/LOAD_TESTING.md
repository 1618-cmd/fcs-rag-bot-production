# Load Testing Guide

This guide explains how to use the load testing script to test the FCS RAG Bot API under concurrent load.

## Overview

The load testing script (`load_test.py`) simulates multiple concurrent users making requests to the API to test:
- System robustness under load
- Response time performance
- Error rates and failure modes
- Throughput capacity
- Resource usage (CPU, memory, database connections)

## Prerequisites

Install dependencies:
```bash
pip install aiohttp
```

Or install all backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

## Basic Usage

### Test with 50 concurrent users for 60 seconds
```bash
python scripts/load_test.py --users 50 --duration 60
```

### Test specific endpoint
```bash
python scripts/load_test.py --users 50 --duration 60 --scenario query
python scripts/load_test.py --users 50 --duration 60 --scenario calc_script
python scripts/load_test.py --users 50 --duration 60 --scenario login
```

### Test against production
```bash
python scripts/load_test.py --url https://fcs-rag-bot-production.onrender.com --users 50 --duration 60
```

### Save results to file
```bash
python scripts/load_test.py --users 50 --duration 60 --save-report
```

## Test Scenarios

### 1. Query Only (`--scenario query`)
- Tests regular RAG queries
- Uses sample questions from knowledge base
- Good for baseline performance testing

### 2. Calc Script Analysis (`--scenario calc_script`)
- Tests calc script analysis feature
- Includes VenaQL script in requests
- Tests script parsing and analysis performance

### 3. Login (`--scenario login`)
- Tests authentication endpoint
- Simulates user logins
- Tests JWT token generation

### 4. Mixed Workload (`--scenario mixed`)
- **Recommended for realistic testing**
- Mix of queries, calc scripts, and logins
- Simulates real-world usage patterns

## Command Line Options

```
--url URL              Base URL of the API (default: http://localhost:8000)
--users N              Number of concurrent users (default: 50)
--duration N           Test duration in seconds (default: 60)
--scenario TYPE        Test scenario: query, calc_script, login, mixed (default: mixed)
--endpoint TYPE        Endpoint filter: query, calc_script, login, all (default: all)
--timeout N            Request timeout in seconds (default: 30)
--save-report          Save results to JSON file
```

## Example Commands

### Baseline Test (50 users, 1 minute)
```bash
python scripts/load_test.py --users 50 --duration 60 --scenario query
```

### Stress Test (100 users, 2 minutes)
```bash
python scripts/load_test.py --users 100 --duration 120 --scenario mixed
```

### Endurance Test (50 users, 10 minutes)
```bash
python scripts/load_test.py --users 50 --duration 600 --scenario mixed
```

### Production Load Test
```bash
python scripts/load_test.py \
  --url https://fcs-rag-bot-production.onrender.com \
  --users 50 \
  --duration 120 \
  --scenario mixed \
  --save-report
```

## Understanding Results

### Metrics Explained

- **Total Requests**: Total number of requests made
- **Successful/Failed**: Number of successful (200) vs failed requests
- **Success Rate**: Percentage of successful requests
- **Response Times**:
  - **Average**: Mean response time
  - **Min/Max**: Fastest and slowest responses
  - **P50 (Median)**: 50% of requests faster than this
  - **P95**: 95% of requests faster than this (important for user experience)
  - **P99**: 99% of requests faster than this (catches outliers)
- **Throughput**: Requests per second
- **Error Breakdown**: Types and counts of errors

### Good Performance Indicators

- **Success Rate**: > 99% (ideally 100%)
- **P95 Response Time**: < 3 seconds for queries
- **P99 Response Time**: < 5 seconds for queries
- **Throughput**: > 10 req/s for 50 users

### Red Flags

- **Success Rate < 95%**: System is struggling
- **P95 > 10 seconds**: Unacceptable user experience
- **Many timeouts**: Backend can't handle load
- **500 errors**: Backend errors, check logs
- **Rate limit errors**: Need to adjust rate limiting

## Interpreting Results

### Example Output

```
📊 LOAD TEST RESULTS - MIXED
============================================================

Total Requests:      1,234
Successful:          1,200
Failed:              34
Success Rate:         97.24%

Response Times:
  Average:            2,345.67 ms
  Min:                450.23 ms
  Max:                8,901.45 ms
  P50 (Median):       2,100.00 ms
  P95:                4,500.00 ms
  P99:                7,200.00 ms

Throughput:          20.57 req/s

Error Breakdown:
  Timeout: 20
  HTTP 500: 10
  HTTP 429: 4
```

### Analysis

- **97.24% success rate**: Good, but could be better
- **P95 of 4.5s**: Acceptable for RAG queries
- **20 timeouts**: May need to increase timeout or optimize backend
- **10 HTTP 500 errors**: Check backend logs for errors
- **4 HTTP 429 errors**: Rate limiting kicking in, may need adjustment

## Tips

1. **Start Small**: Test with 10 users first, then scale up
2. **Monitor Backend**: Watch CPU, memory, and database connections during test
3. **Check Logs**: Review backend logs for errors during load test
4. **Compare Scenarios**: Test different scenarios to find bottlenecks
5. **Production Testing**: Always test against production during off-peak hours
6. **Save Reports**: Use `--save-report` to track performance over time

## Troubleshooting

### "Connection refused"
- Backend is not running
- Wrong URL specified
- Firewall blocking connection

### "Timeout" errors
- Backend is too slow
- Increase `--timeout` value
- Check backend performance

### "Too many open files"
- System limit reached
- Reduce `--users` count
- Increase system file descriptor limit

### High error rates
- Backend is overloaded
- Database connection pool exhausted
- Rate limiting too aggressive
- Check backend logs

## Next Steps

After load testing:
1. Review metrics and identify bottlenecks
2. Optimize slow endpoints
3. Adjust rate limiting if needed
4. Scale infrastructure if necessary
5. Re-test after optimizations
