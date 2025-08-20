"""
Portfolio Data Loading Module

This module handles loading portfolio data from YAML files and validating it
using Pydantic models. It provides error handling and fallback mechanisms.
"""

import os
import yaml
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, ValidationError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic Models for Data Validation
class Experience(BaseModel):
    company: str
    position: str
    duration: str
    location: str
    period: str
    achievements: List[str]

class Education(BaseModel):
    institution: str
    degree: str
    period: str
    location: str

class Skill(BaseModel):
    name: str
    category: str

class Certification(BaseModel):
    name: str
    issuer: str

class PersonalInfo(BaseModel):
    name: str
    title: str
    location: str
    summary: str
    email: str
    linkedin: str
    github: str
    profile: str

class PortfolioData(BaseModel):
    personal: PersonalInfo
    experience: List[Experience]
    education: List[Education]
    skills: List[Skill]
    certifications: List[Certification]

def load_profile_data(profile_path: Optional[str] = None) -> PortfolioData:
    """
    Load portfolio data from YAML file.
    
    Args:
        profile_path: Path to the YAML file. If None, uses default locations.
    
    Returns:
        PortfolioData: Validated portfolio data
        
    Raises:
        FileNotFoundError: If profile file is not found
        ValidationError: If YAML data doesn't match expected schema
        yaml.YAMLError: If YAML file is malformed
    """
    # Determine profile file path
    if profile_path is None:
        profile_path = "portfolio.yml"
        
        if not os.path.exists(profile_path):
            raise FileNotFoundError(
                f"Portfolio file not found: {profile_path}. "
                "Please create 'portfolio.yml' in the project root with your portfolio data. "
                "See README.md for setup instructions."
            )
    
    # Load YAML file
    try:
        with open(profile_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
            logger.info(f"Successfully loaded profile data from {profile_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {profile_path}: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Profile file not found: {profile_path}")
    
    # Validate data using Pydantic
    try:
        portfolio_data = PortfolioData(**yaml_data)
        logger.info(f"Successfully validated portfolio data for {portfolio_data.personal.name}")
        return portfolio_data
    except ValidationError as e:
        logger.error(f"Validation error in profile data: {e}")
        raise e

def get_portfolio_data() -> PortfolioData:
    """
    Get portfolio data with error handling and fallback.
    
    Returns:
        PortfolioData: Portfolio data loaded from YAML
        
    Raises:
        RuntimeError: If data cannot be loaded
    """
    try:
        return load_profile_data()
    except (FileNotFoundError, ValidationError, yaml.YAMLError) as e:
        logger.error(f"Failed to load portfolio data: {e}")
        raise RuntimeError(f"Failed to load portfolio data: {e}")

# Global instance for caching
_portfolio_data: Optional[PortfolioData] = None

def get_cached_portfolio_data() -> PortfolioData:
    """
    Get cached portfolio data. Loads once and caches for subsequent calls.
    
    Returns:
        PortfolioData: Cached portfolio data
    """
    global _portfolio_data
    if _portfolio_data is None:
        _portfolio_data = get_portfolio_data()
    return _portfolio_data

def reload_portfolio_data() -> PortfolioData:
    """
    Force reload of portfolio data from YAML file.
    
    Returns:
        PortfolioData: Freshly loaded portfolio data
    """
    global _portfolio_data
    _portfolio_data = get_portfolio_data()
    return _portfolio_data
