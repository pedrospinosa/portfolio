from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging

from .data import load_portfolio_data

logger = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request, portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return templates.TemplateResponse("index.html", {"request": request, "portfolio": portfolio_data})


@router.get("/api/portfolio")
async def portfolio(portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data


@router.get("/api/experience")
async def experience(portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.experience


@router.get("/api/skills")
async def skills(portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.skills


@router.get("/api/education")
async def education(portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.education


@router.get("/api/certifications")
async def certifications(portfolio_data=Depends(load_portfolio_data)):
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.certifications
