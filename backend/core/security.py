import time
import re
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response

# Rate limiting configuration
RATE_LIMIT = 60
RATE_LIMIT_WINDOW = 60
ip_buckets = {}

def check_rate_limit(ip: str) -> bool:
    now = time.time()
    if ip not in ip_buckets:
        ip_buckets[ip] = {'tokens': RATE_LIMIT, 'last_update': now}
    
    bucket = ip_buckets[ip]
    elapsed = now - bucket['last_update']
    
    bucket['tokens'] += elapsed * (RATE_LIMIT / RATE_LIMIT_WINDOW)
    if bucket['tokens'] > RATE_LIMIT:
        bucket['tokens'] = RATE_LIMIT
    
    bucket['last_update'] = now
    
    if bucket['tokens'] >= 1:
        bucket['tokens'] -= 1
        return False
    return True

# Malicious patterns for XSS/SQLi blocking
MALICIOUS_PATTERNS = [
    re.compile(r"<script.*?>.*?</script.*?>", re.IGNORECASE),
    re.compile(r"javascript:", re.IGNORECASE),
    re.compile(r"onload=", re.IGNORECASE),
    re.compile(r"onerror=", re.IGNORECASE),
    re.compile(r"SELECT\s+.*?\s+FROM", re.IGNORECASE),
    re.compile(r"UNION\s+ALL\s+SELECT", re.IGNORECASE),
    re.compile(r"DROP\s+TABLE", re.IGNORECASE)
]

class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Rate Limiting
        client_ip = request.client.host if request.client else "unknown"
        if check_rate_limit(client_ip):
            return JSONResponse(status_code=429, content={"success": False, "message": "Too Many Requests"})

        # 2. Path Traversal & Anti-Bot
        path = request.url.path
        if ".." in path or "%2e%2e" in path.lower():
            return JSONResponse(status_code=403, content={"success": False, "message": "Forbidden Path"})

        user_agent = request.headers.get('User-Agent', '').lower()
        blocked_agents = ['python-requests', 'curl', 'wget', 'urllib', 'bot', 'spider', 'scraper', 'headless']
        if any(bot in user_agent for bot in blocked_agents):
            return JSONResponse(status_code=403, content={"success": False, "message": "Automated access denied"})

        # 3. Request Payload Scanning (for POST/PUT)
        if request.method in ["POST", "PUT"]:
            content_length = request.headers.get("Content-Length")
            if content_length and int(content_length) > 2 * 1024 * 1024:
                return JSONResponse(status_code=413, content={"success": False, "message": "Payload Too Large"})
            
            # Read body to check for malicious patterns, then rewrite it for the actual endpoint
            body = await request.body()
            body_str = body.decode("utf-8", errors="ignore")
            for pattern in MALICIOUS_PATTERNS:
                if pattern.search(body_str):
                    return JSONResponse(status_code=403, content={"success": False, "message": "Malicious payload detected"})
            
            async def receive():
                return {"type": "http.request", "body": body}
            request._receive = receive

        # 4. Proceed with request
        response: Response = await call_next(request)

        # 5. Inject 10x Security Headers
        response.headers["Content-Security-Policy"] = "default-src 'self' 'unsafe-inline' 'unsafe-eval' https: data:;"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        response.headers["X-XSS-Protection"] = "1; mode=block"

        return response
