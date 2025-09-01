import logging
from collections import Counter

import yaml
from pydantic import BaseModel

from config import DEFAULT_PORTFOLIO_PATH

logger = logging.getLogger(__name__)


class Experience(BaseModel):
    company: str
    position: str
    duration: str
    location: str
    period: str
    achievements: list[str]


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
    experience: list[Experience]
    education: list[Education]
    skills: list[Skill]
    certifications: list[Certification]


_portfolio_data: PortfolioData | None = None


def load_portfolio_data(
    profile_path: str = DEFAULT_PORTFOLIO_PATH, use_cache: bool = True
) -> PortfolioData:
    global _portfolio_data

    if use_cache and _portfolio_data is not None:
        return _portfolio_data

    with open(profile_path, encoding="utf-8") as file:
        yaml_data = yaml.safe_load(file)

    portfolio_data = PortfolioData(**yaml_data)

    try:
        if portfolio_data.skills:
            category_counts: Counter[str] = Counter(
                skill.category for skill in portfolio_data.skills
            )

            portfolio_data.skills.sort(
                key=lambda s: (-category_counts.get(s.category, 0), s.name.lower())
            )
    except Exception:
        pass

    if use_cache:
        _portfolio_data = portfolio_data

    return portfolio_data
