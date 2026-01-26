"""
Vena API service for reading data from Vena tenant.

Provides read-only access to Vena tenant data to enhance RAG responses
with real-time model structure, dimensions, and metadata.

Uses HTTP Basic Auth with apiUser/apiKey credentials.
Endpoint format: https://{hub}.vena.io/api/public/v1/
"""

import logging
import httpx
import json
from typing import Optional, Dict, List, Any
from ..utils.config import settings

logger = logging.getLogger(__name__)


class VenaAPIClient:
    """Client for interacting with Vena API (read-only operations)."""
    
    def __init__(self):
        """Initialize Vena API client with credentials from settings."""
        self.api_user = settings.vena_api_user
        self.api_key = settings.vena_api_key
        self.tenant_name = settings.vena_tenant_name
        # Compute base URL from hub if not explicitly set
        if settings.vena_api_base_url:
            self.base_url = settings.vena_api_base_url
        elif settings.vena_api_hub:
            self.base_url = f"https://{settings.vena_api_hub}.vena.io/api/public/v1"
        else:
            self.base_url = None
        
        if not self.api_user or not self.api_key or not self.base_url:
            logger.warning("Vena API credentials not fully configured. Vena API features will be disabled.")
            self.enabled = False
        else:
            self.enabled = True
            logger.info(f"Vena API client initialized for tenant: {self.tenant_name} at {self.base_url}")
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for Vena API requests."""
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    
    def _get_auth(self) -> tuple:
        """Get Basic Auth credentials for Vena API.
        
        Returns:
            Tuple of (username, password) for HTTP Basic Auth
        """
        return (self.api_user, self.api_key)
    
    async def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Make a request to the Vena API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path (e.g., '/models/{modelID}/intersections')
            params: Query parameters
            json_data: JSON body for POST requests
            
        Returns:
            Response JSON data or None if error
        """
        if not self.enabled:
            return None
        
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        try:
            async with httpx.AsyncClient(timeout=30.0, auth=self._get_auth()) as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=self._get_headers(),
                    params=params,
                    json=json_data
                )
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 401:
                    logger.warning(f"Vena API authentication failed (401) for {endpoint}")
                    return None
                elif response.status_code == 403:
                    logger.warning(f"Vena API permission denied (403) for {endpoint}")
                    return None
                elif response.status_code == 404:
                    logger.debug(f"Vena API endpoint not found (404): {endpoint}")
                    return None
                else:
                    logger.warning(
                        f"Vena API returned status {response.status_code} for {endpoint}: "
                        f"{response.text[:200]}"
                    )
                    return None
                    
        except Exception as e:
            logger.error(f"Error calling Vena API endpoint {endpoint}: {e}")
            return None
    
    async def get_intersections(
        self, 
        model_id: str, 
        filters: Optional[List[Dict[str, Any]]] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Get intersection data from a Vena model.
        
        This is the PRIMARY endpoint available in the Vena Public API.
        
        Args:
            model_id: The model ID (get from Vena UI: Modeler -> Data Model -> check URL)
            filters: Optional list of filter dictionaries
                    Example: [{"field": "Year", "eq": "2023"}]
            fields: Optional list of field names to return (comma-separated string)
            limit: Optional limit for pagination (default: API default)
            offset: Optional offset for pagination (default: 0)
            
        Returns:
            List of intersection dictionaries or None if error
        """
        endpoint = f"models/{model_id}/intersections"
        params = {}
        
        if filters:
            # Filters must be lowercase 'filters' parameter, JSON-encoded
            import json
            params['filters'] = json.dumps(filters)
        
        if fields:
            # Fields can be a list or comma-separated string
            if isinstance(fields, list):
                params['fields'] = ','.join(fields)
            else:
                params['fields'] = fields
        
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        data = await self._make_request('GET', endpoint, params=params)
        # API returns a list of intersections
        if data:
            return data if isinstance(data, list) else [data]
        return None
    
    async def get_model_structure(self, model_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get model structure/metadata.
        
        NOTE: The Vena Public API does not have a direct model structure endpoint.
        Structure can be inferred from intersection data.
        
        Args:
            model_id: Model ID (required)
            
        Returns:
            Model structure dictionary inferred from intersections, or None if error
        """
        if not model_id:
            logger.warning("get_model_structure requires model_id")
            return None
        
        try:
            # Get a sample of intersections to infer structure
            intersections = await self.get_intersections(model_id, filters=None, fields=None, limit=1)
            if intersections and isinstance(intersections, list) and len(intersections) > 0:
                first_intersection = intersections[0]
                if isinstance(first_intersection, dict):
                    # Extract dimensions from intersection keys
                    excluded_fields = {'Value', 'value', 'id', '_id'}
                    dimensions = [key for key in first_intersection.keys() if key not in excluded_fields]
                    
                    return {
                        "modelId": model_id,
                        "dimensions": [{"name": dim} for dim in dimensions],
                        "note": "Structure inferred from intersection data - Vena Public API does not provide direct model structure endpoint"
                    }
            return None
        except Exception as e:
            logger.warning(f"Could not infer model structure from intersections: {e}")
            return None
    
    async def get_dimensions(self, model_id: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Get list of dimensions for a model.
        
        NOTE: The Vena Public API does not have a direct dimensions endpoint.
        Dimensions must be extracted from intersection data.
        
        Args:
            model_id: Model ID (required to get intersections)
            
        Returns:
            List of dimension names extracted from intersections, or None if error
        """
        if not model_id:
            logger.warning("get_dimensions requires model_id - cannot extract dimensions without model")
            return None
        
        # Extract dimensions from a sample intersection query
        try:
            intersections = await self.get_intersections(model_id, filters=None, fields=None, limit=1)
            if intersections and isinstance(intersections, list) and len(intersections) > 0:
                # Extract dimension names from first intersection keys
                first_intersection = intersections[0]
                if isinstance(first_intersection, dict):
                    # Filter out common non-dimension fields
                    excluded_fields = {'Value', 'value', 'id', '_id'}
                    dimensions = [key for key in first_intersection.keys() if key not in excluded_fields]
                    return [{"name": dim} for dim in dimensions]
            return None
        except Exception as e:
            logger.warning(f"Could not extract dimensions from intersections: {e}")
            return None
    
    async def get_dimension_members(
        self, 
        dimension_name: str, 
        model_id: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Get members of a specific dimension.
        
        NOTE: The Vena Public API does not have a direct dimension members endpoint.
        Members must be extracted from intersection data.
        
        Args:
            dimension_name: Name of the dimension (e.g., "Account", "Entity")
            model_id: Model ID (required)
            
        Returns:
            List of unique dimension member values from intersections, or None if error
        """
        if not model_id:
            logger.warning("get_dimension_members requires model_id")
            return None
        
        try:
            # Get intersections and extract unique values for the dimension
            # Use limit to avoid fetching too much data
            intersections = await self.get_intersections(model_id, filters=None, fields=[dimension_name], limit=1000)
            if intersections and isinstance(intersections, list):
                # Extract unique values for this dimension
                members = set()
                for intersection in intersections:
                    if isinstance(intersection, dict) and dimension_name in intersection:
                        value = intersection[dimension_name]
                        if value:
                            members.add(str(value))
                
                # Return as list of dicts with name field
                return [{"name": member} for member in sorted(members)]
            return None
        except Exception as e:
            logger.warning(f"Could not extract {dimension_name} members from intersections: {e}")
            return None
    
    async def get_etl_templates(self) -> Optional[List[Dict[str, Any]]]:
        """
        Get list of ETL templates.
        
        NOTE: The Vena Public API does not have a templates listing endpoint.
        Template IDs must be obtained from the Vena UI (Modeler → ETL → Templates).
        
        Returns:
            None (endpoint not available in public API)
        """
        logger.warning("ETL templates endpoint not available in Vena Public API. Template IDs must be obtained from Vena UI.")
        return None
    
    async def get_etl_jobs(self, template_id: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Get list of ETL jobs.
        
        NOTE: The Vena Public API does not have a jobs listing endpoint.
        Jobs are created via POST /jobs/start-with-data and return a jobId.
        
        Args:
            template_id: Not used (endpoint doesn't exist)
            
        Returns:
            None (endpoint not available in public API)
        """
        logger.warning("ETL jobs listing endpoint not available in Vena Public API. Jobs are created via POST /jobs/start-with-data.")
        return None
    
    async def _detect_vena_intent(self, question: str) -> Dict[str, Any]:
        """
        Use LLM to intelligently detect what Vena data is needed from vague questions.
        
        Args:
            question: User's question
            
        Returns:
            Dict with intent detection results: {
                'needs_dimensions': bool,
                'needs_hierarchies': bool,
                'needs_intersections': bool,
                'needs_etl': bool,
                'dimension_types': List[str],  # e.g., ['Account', 'Entity']
                'needs_model_structure': bool
            }
        """
        try:
            from openai import AsyncOpenAI
            
            client = AsyncOpenAI(api_key=settings.openai_api_key)
            
            intent_prompt = f"""Analyze this question and determine what Vena tenant data would be helpful to answer it.

Question: "{question}"

Based on the question, determine what Vena data to fetch. Return ONLY a JSON object with this exact structure:
{{
    "needs_dimensions": true/false,
    "needs_hierarchies": true/false,
    "needs_intersections": true/false,
    "needs_etl": true/false,
    "dimension_types": ["Account", "Entity"] or [],
    "needs_model_structure": true/false
}}

Guidelines:
- "needs_dimensions": true if question asks about dimensions, members, or structure
- "needs_hierarchies": true if question mentions hierarchies, roll-ups, parent/child, or "my accounts/entities"
- "needs_intersections": true if question asks about data values, amounts, or specific intersections
- "needs_etl": true if question mentions ETL, templates, jobs, import, or export
- "dimension_types": List specific dimension types mentioned (Account, Entity, Period, Measure, Scenario, etc.)
- "needs_model_structure": true if question asks about "my model", "what's in my model", or general structure

Examples:
- "show me my stuff" -> {{"needs_dimensions": true, "needs_hierarchies": true, "dimension_types": []}}
- "what accounts do I have?" -> {{"needs_dimensions": true, "needs_hierarchies": true, "dimension_types": ["Account"]}}
- "what's in my model?" -> {{"needs_dimensions": true, "needs_model_structure": true, "dimension_types": []}}
- "help me build a script for my entities" -> {{"needs_dimensions": true, "needs_hierarchies": true, "dimension_types": ["Entity"]}}

Return ONLY the JSON object, no other text."""

            response = await client.chat.completions.create(
                model="gpt-4o-mini",  # Use cheaper model for intent detection
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes questions to determine what Vena API data to fetch. Return only valid JSON."},
                    {"role": "user", "content": intent_prompt}
                ],
                temperature=0.1,
                max_tokens=200
            )
            
            content = response.choices[0].message.content.strip()
            
            # Extract JSON from response (handle markdown code blocks)
            if "```" in content:
                # Extract JSON from code block
                json_start = content.find("{")
                json_end = content.rfind("}") + 1
                if json_start >= 0 and json_end > json_start:
                    content = content[json_start:json_end]
            
            intent = json.loads(content)
            logger.info(f"Detected Vena intent: {intent}")
            return intent
            
        except Exception as e:
            logger.warning(f"LLM intent detection failed, falling back to keyword detection: {e}")
            # Fallback to keyword-based detection
            return self._keyword_based_intent(question)
    
    def _keyword_based_intent(self, question: str) -> Dict[str, Any]:
        """
        Fallback keyword-based intent detection.
        
        Args:
            question: User's question
            
        Returns:
            Intent dict
        """
        question_lower = question.lower()
        
        # Detect dimension types mentioned
        dimension_types = []
        dimension_keywords = {
            'account': 'Account',
            'entity': 'Entity',
            'period': 'Period',
            'measure': 'Measure',
            'scenario': 'Scenario',
            'counterparty': 'Counterparty',
            'currency': 'Currency'
        }
        
        for keyword, dim_name in dimension_keywords.items():
            if keyword in question_lower:
                dimension_types.append(dim_name)
        
        return {
            'needs_dimensions': any(kw in question_lower for kw in ['dimension', 'member', 'account', 'entity', 'period', 'measure', 'scenario', 'stuff', 'model']),
            'needs_hierarchies': any(kw in question_lower for kw in ['hierarchy', 'hierarchies', 'roll-up', 'parent', 'child', 'my accounts', 'my entities']),
            'needs_intersections': any(kw in question_lower for kw in ['value', 'data', 'amount', 'revenue', 'expense', 'intersection']),
            'needs_etl': any(kw in question_lower for kw in ['etl', 'template', 'job', 'import', 'export']),
            'dimension_types': dimension_types,
            'needs_model_structure': any(kw in question_lower for kw in ['model', 'structure', 'what\'s in', 'show me my'])
        }
    
    async def format_vena_context(self, question: str, model_id: Optional[str] = None) -> Optional[str]:
        """
        Intelligently fetch relevant Vena data based on the question
        using LLM-based intent detection for vague questions.
        
        Args:
            question: User's question to determine what Vena data to fetch
            model_id: Optional model ID to use for queries
            
        Returns:
            Formatted context string with relevant Vena data, or None
        """
        if not self.enabled:
            return None
        
        context_parts = []
        
        try:
            # Use LLM to detect intent (with caching to avoid extra calls)
            from ..services.cache import get_cached_response, cache_response
            
            # Check cache for intent detection
            intent_cache_key = f"vena_intent:{question.lower()}"
            cached_intent = get_cached_response(intent_cache_key)
            
            if cached_intent:
                intent = cached_intent.get('answer', {})
                logger.info("Using cached intent detection")
            else:
                # Detect intent using LLM
                intent = await self._detect_vena_intent(question)
                # Cache intent (24 hour TTL - intent doesn't change)
                cache_response(intent_cache_key, {
                    'answer': intent,
                    'sources': [],
                    'latency_ms': 0,
                    'model': 'intent-detection'
                }, ttl_seconds=86400)
            
            # Fetch data based on detected intent
            
            # NOTE: Most Vena API endpoints don't exist - we can only use intersections
            # To get dimensions/members, we need to extract them from intersection data
            # This requires a model_id, which we may not have
            
            # If we have a model_id, we can extract dimensions from intersections
            if model_id:
                # Fetch dimensions if needed (extracted from intersections)
                if intent.get('needs_dimensions') or intent.get('needs_model_structure'):
                    dimensions = await self.get_dimensions(model_id)
                    if dimensions:
                        context_parts.append(f"Available Dimensions: {[d.get('name', d) for d in dimensions[:10]]}")
                
                # Fetch specific dimension members if types are specified
                dimension_types = intent.get('dimension_types', [])
                if dimension_types:
                    for dim_type in dimension_types:
                        members = await self.get_dimension_members(dim_type, model_id)
                        if members:
                            context_parts.append(f"{dim_type} Dimension Members (sample): {[m.get('name', m) for m in members[:20]]}")
                
                # Fetch hierarchies if needed (extracted from intersections)
                if intent.get('needs_hierarchies'):
                    # If specific dimension types mentioned, get those members
                    if dimension_types:
                        for dim_type in dimension_types:
                            members = await self.get_dimension_members(dim_type, model_id)
                            if members:
                                context_parts.append(f"{dim_type} Members (sample): {[m.get('name', m) for m in members[:30]]}")
                    else:
                        # Get all dimensions for hierarchy context
                        dimensions = await self.get_dimensions(model_id)
                        if dimensions:
                            # Get members for first few dimensions
                            for dim in dimensions[:3]:
                                dim_name = dim.get('name') if isinstance(dim, dict) else str(dim)
                                members = await self.get_dimension_members(dim_name, model_id)
                                if members:
                                    context_parts.append(f"{dim_name} Members (sample): {[m.get('name', m) for m in members[:20]]}")
                
                # Fetch intersections if needed
                if intent.get('needs_intersections'):
                    # Try to extract filters from question
                    filters = []
                    if '2023' in question or '2024' in question or '2025' in question:
                        year = next((y for y in ['2023', '2024', '2025'] if y in question), None)
                        if year:
                            filters.append({"field": "Year", "eq": year})
                    
                    intersections = await self.get_intersections(model_id, filters=filters if filters else None, limit=10)
                    if intersections:
                        context_parts.append(f"Model Intersections (sample of 10): {intersections[:10]}")
                
                # Fetch model structure if needed (inferred from intersections)
                if intent.get('needs_model_structure'):
                    structure = await self.get_model_structure(model_id)
                    if structure:
                        context_parts.append(f"Model Structure (inferred): {structure}")
            else:
                # No model_id - can't fetch data
                logger.warning("Cannot fetch Vena data without model_id. Most Vena API operations require a model ID.")
                context_parts.append("IMPORTANT: To answer questions about your Vena tenant data (dimensions, hierarchies, accounts, etc.), a Model ID is required. The user asked about their tenant data, but no Model ID was provided. Please inform the user that they need to provide their Model ID. You can find your Model ID in Vena: Modeler -> Data Model -> check the URL (the number at the end of the URL is the Model ID).")
            
            # ETL endpoints don't exist in public API
            if intent.get('needs_etl'):
                context_parts.append("Note: ETL template and job listing endpoints are not available in the Vena Public API. Template IDs must be obtained from the Vena UI (Modeler -> ETL -> Templates).")
            
            if context_parts:
                formatted_context = "\n\n--- Vena Tenant Data (Live) ---\n\n" + "\n\n".join(context_parts)
                logger.info("Generated Vena context for question")
                return formatted_context
            
            return None
            
        except Exception as e:
            logger.error(f"Error generating Vena context: {e}", exc_info=True)
            # Fallback to keyword-based detection
            try:
                intent = self._keyword_based_intent(question)
                logger.info(f"Using fallback keyword detection: {intent}")
                # Retry with keyword-based intent (simplified)
                if intent.get('needs_dimensions'):
                    dimensions = await self.get_dimensions(model_id)
                    if dimensions:
                        return f"\n\n--- Vena Tenant Data (Live) ---\n\nAvailable Dimensions: {dimensions[:10]}"
            except Exception as fallback_error:
                logger.error(f"Fallback also failed: {fallback_error}")
            
            return None


# Global client instance
_vena_client: Optional[VenaAPIClient] = None


def get_vena_client() -> Optional[VenaAPIClient]:
    """Get or create Vena API client instance."""
    global _vena_client
    if _vena_client is None:
        _vena_client = VenaAPIClient()
    return _vena_client if _vena_client.enabled else None
