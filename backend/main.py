import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.api.routes import router as api_router
from backend.core.security import SecurityMiddleware

app = FastAPI(title="Kensington Ivy API")

# Add Security Middleware
app.add_middleware(SecurityMiddleware)

# Add CORS Middleware (Restrictive)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "https://www.kensingtonivy.co.uk"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

# Static File Mounting
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.mount("/css", StaticFiles(directory=os.path.join(base_dir, "css")), name="css")
app.mount("/assets", StaticFiles(directory=os.path.join(base_dir, "assets")), name="assets")
app.mount("/pages", StaticFiles(directory=os.path.join(base_dir, "pages"), html=True), name="pages")

@app.get("/")
async def read_index():
    with open(os.path.join(base_dir, "index.html"), "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/{file_path:path}")
async def catch_all(file_path: str):
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path) and os.path.isfile(full_path):
        if file_path.endswith('.html'):
            with open(full_path, "r") as f:
                return HTMLResponse(content=f.read(), status_code=200)
    return HTMLResponse(content="<h1>404 - Not Found</h1>", status_code=404)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=5173, reload=True)
