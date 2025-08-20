from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

# Import our data loading module
from .data import get_cached_portfolio_data, reload_portfolio_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Portfolio", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Load portfolio data
try:
    portfolio_data = get_cached_portfolio_data()
    logger.info(f"Successfully loaded portfolio data for {portfolio_data.personal.name}")
except Exception as e:
    logger.error(f"Failed to load portfolio data: {e}")
    portfolio_data = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return templates.TemplateResponse("index.html", {"request": request, "portfolio": portfolio_data})

@app.get("/api/portfolio")
async def get_portfolio():
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data

@app.get("/api/experience")
async def get_experience():
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.experience

@app.get("/api/skills")
async def get_skills():
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.skills

@app.get("/api/education")
async def get_education():
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.education

@app.get("/api/certifications")
async def get_certifications():
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.certifications


def main():
    """Main function to run the portfolio server"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def dev():
    """Development function to run the portfolio server with auto-reload"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main() 