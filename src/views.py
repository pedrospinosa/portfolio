import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .data import PortfolioData, load_portfolio_data

logger = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(
    request: Request, portfolio_data: PortfolioData = Depends(load_portfolio_data)
) -> Any:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return templates.TemplateResponse(
        "index.html", {"request": request, "portfolio": portfolio_data}
    )


@router.get("/api/portfolio")
async def portfolio(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> PortfolioData:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data


@router.get("/api/experience")
async def experience(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> list[Any]:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.experience


@router.get("/api/skills")
async def skills(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> list[Any]:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.skills


@router.get("/api/education")
async def education(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> list[Any]:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.education


@router.get("/api/certifications")
async def certifications(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> list[Any]:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.certifications


@router.get("/api/projects")
async def projects(portfolio_data: PortfolioData = Depends(load_portfolio_data)) -> list[Any]:
    if portfolio_data is None:
        raise HTTPException(status_code=500, detail="Portfolio data not available")
    return portfolio_data.projects
