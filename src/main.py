from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(title="Pedro Spinosa Portfolio", version="1.0.0")

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

# Portfolio data models
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

class PortfolioData(BaseModel):
    name: str
    title: str
    location: str
    summary: str
    email: str
    linkedin: str
    github: str
    experience: List[Experience]
    education: List[Education]
    skills: List[Skill]
    certifications: List[Certification]
    profile_picture_url: str

# Portfolio data
portfolio_data = PortfolioData(
    name="Pedro Spinosa",
    title="ML Engineer @ Nubank | AI Platform | MLOps & Infra",
    location="Brazil",
    summary="I am a software engineer with a strong background in AI and Machine Learning, passionate about building reliable, scalable ML Platform infrastructure and DevOps solutions. For almost three years, I've been working on an AI Platform team, building tools and frameworks that boost productivity and scalability for ML and data science teams, contributing to ML operations. I aim to apply my skills in software development, ML, and large‑scale production systems to create impactful solutions.",
    email="spinosaphb@gmail.com",
    linkedin="www.linkedin.com/in/pedrospinosa",
    github="github.com/spinosaphb",
    experience=[
        Experience(
            company="Nubank",
            position="Machine Learning Engineer",
            duration="2 years 11 months",
            location="São Paulo, São Paulo, Brazil",
            period="September 2024 - Present (11 months)",
            achievements=[
                "Built an integration service that enables third-party model deployment within the current infrastructure, supporting the addition of state-of-the-art LLM models and automating the onboarding workflow for external models",
                "Provided ongoing support and enhancements to the current ML development tool, adapting it to meet evolving use cases and optimizing the model training and scoring workflows",
                "Developed technical reference materials and documentation for AI infrastructure, conducted tool training for development teams, and maintained ongoing feedback loops with users to continuously improve MLOps solutions"
            ]
        ),
        Experience(
            company="Nubank",
            position="Junior Machine Learning Engineer",
            duration="8 months",
            location="São Paulo, São Paulo, Brazil",
            period="January 2024 - August 2024",
            achievements=[
                "Implemented a lifecycle process for Python versions, enabling reliability of models and libraries, along with updating all AI platform libraries to comply with updated Python range versions",
                "Led performance optimization initiatives, achieving significant latency reductions in model inference, enabling multi-parallelism and scoring in batch",
                "Enhancing our model development tool to better align with user experience requirements, while also strengthening foundational processes to improve the overall development experience—particularly for new users entering the system"
            ]
        ),
        Experience(
            company="Nubank",
            position="Machine Learning Engineering Intern",
            duration="1 year 4 months",
            location="São Paulo, São Paulo, Brazil",
            period="September 2022 - December 2023",
            achievements=[
                "Developed standardized containerization patterns for ML model deployment, improving resource utilization",
                "Built foundational REST API endpoints for model serving, streamlining deployment workflows",
                "Contributed to team knowledge sharing, enhancing documentation and best practices in ML infrastructure"
            ]
        ),
        Experience(
            company="Insight Data Science Lab",
            position="Machine Learning Researcher",
            duration="1 year 4 months",
            location="Fortaleza, Ceará, Brazil",
            period="May 2021 - August 2022",
            achievements=[
                "Developed an application that utilizes Named Entity Recognition to identify and highlight entities within a text‑based bulletin. To achieve this, the API utilizes two libraries/frameworks for building base models: SpaCy and Keras",
                "Developed an ML operation tool implemented as a class enabling parallel or queued machine learning model training, resulting in a productivity increase of at least 50% by utilizing background threads",
                "Created a testable and reliable monitoring class using WebSockets, providing real‑time updates on machine learning model training progress and performance during each epoch for improved ML operations visibility"
            ]
        )
    ],
    education=[
        Education(
            institution="Federal University of Ceara",
            degree="Bachelor's degree, Computer Science",
            period="2019 - 2023",
            location="Fortaleza, Ceará, Brazil"
        )
    ],
    skills=[
        Skill(name="Deep Learning", category="AI/ML"),
        Skill(name="NLP/NER", category="AI/ML"),
        Skill(name="Docker", category="DevOps"),
        Skill(name="FastAPI", category="Backend"),
        Skill(name="Python", category="Programming"),
        Skill(name="Machine Learning", category="AI/ML"),
        Skill(name="MLOps", category="DevOps"),
        Skill(name="AWS", category="Cloud"),
        Skill(name="REST APIs", category="Backend"),
        Skill(name="Containerization", category="DevOps"),
        Skill(name="Performance Optimization", category="Engineering"),
        Skill(name="Documentation", category="Soft Skills"),
        Skill(name="Team Collaboration", category="Soft Skills")
    ],
    certifications=[
        Certification(name="AWS Academy Machine Learning Foundations", issuer="AWS"),
        Certification(name="AWS Academy Cloud Foundations", issuer="AWS")
    ],
    profile_picture_url="static/assets/profile.png"
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "portfolio": portfolio_data})

@app.get("/api/portfolio")
async def get_portfolio():
    return portfolio_data

@app.get("/api/experience")
async def get_experience():
    return portfolio_data.experience

@app.get("/api/skills")
async def get_skills():
    return portfolio_data.skills

@app.get("/api/education")
async def get_education():
    return portfolio_data.education

@app.get("/api/certifications")
async def get_certifications():
    return portfolio_data.certifications

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 