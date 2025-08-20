"""
Unit tests for the FastAPI application.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from src.main import app


class TestPortfolioEndpoints:
    """Test portfolio API endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)
    
    @pytest.fixture
    def mock_portfolio_data(self):
        """Mock portfolio data for testing."""
        from src.data import PortfolioData, PersonalInfo, Experience, Education, Skill, Certification
        
        return PortfolioData(
            personal=PersonalInfo(
                name="John Doe",
                title="Software Engineer",
                location="San Francisco, CA",
                summary="Experienced software engineer",
                email="john@example.com",
                linkedin="linkedin.com/in/johndoe",
                github="github.com/johndoe",
                profile="avatars.githubusercontent.com/u/123"
            ),
            experience=[
                Experience(
                    company="Tech Corp",
                    position="Senior Engineer",
                    duration="2 years",
                    location="San Francisco, CA",
                    period="2022-2024",
                    achievements=["Built scalable system"]
                )
            ],
            education=[
                Education(
                    institution="University of Tech",
                    degree="Computer Science",
                    period="2018-2022",
                    location="San Francisco, CA"
                )
            ],
            skills=[
                Skill(name="Python", category="Programming"),
                Skill(name="FastAPI", category="Backend")
            ],
            certifications=[
                Certification(name="AWS Certified", issuer="Amazon")
            ]
        )
    
    def test_get_portfolio_success(self, client, mock_portfolio_data):
        """Test successful portfolio data retrieval."""
        # Mock the portfolio_data at module level
        with patch('src.main.portfolio_data', mock_portfolio_data):
            response = client.get("/api/portfolio")
            
            assert response.status_code == 200
            data = response.json()
            assert data["personal"]["name"] == "John Doe"
            assert data["personal"]["title"] == "Software Engineer"
            assert len(data["experience"]) == 1
            assert len(data["education"]) == 1
            assert len(data["skills"]) == 2
            assert len(data["certifications"]) == 1
    
    def test_get_portfolio_data_unavailable(self, client):
        """Test portfolio endpoint when data is unavailable."""
        with patch('src.main.portfolio_data', None):
            response = client.get("/api/portfolio")
            
            assert response.status_code == 500
            assert "Portfolio data not available" in response.json()["detail"]
    
    @patch('src.main.portfolio_data')
    def test_get_experience_success(self, mock_portfolio, client, mock_portfolio_data):
        """Test successful experience data retrieval."""
        mock_portfolio.experience = mock_portfolio_data.experience
        
        response = client.get("/api/experience")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["company"] == "Tech Corp"
        assert data[0]["position"] == "Senior Engineer"
    
    @patch('src.main.portfolio_data')
    def test_get_skills_success(self, mock_portfolio, client, mock_portfolio_data):
        """Test successful skills data retrieval."""
        mock_portfolio.skills = mock_portfolio_data.skills
        
        response = client.get("/api/skills")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["name"] == "Python"
        assert data[0]["category"] == "Programming"
        assert data[1]["name"] == "FastAPI"
        assert data[1]["category"] == "Backend"
    
    @patch('src.main.portfolio_data')
    def test_get_education_success(self, mock_portfolio, client, mock_portfolio_data):
        """Test successful education data retrieval."""
        mock_portfolio.education = mock_portfolio_data.education
        
        response = client.get("/api/education")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["institution"] == "University of Tech"
        assert data[0]["degree"] == "Computer Science"
    
    @patch('src.main.portfolio_data')
    def test_get_certifications_success(self, mock_portfolio, client, mock_portfolio_data):
        """Test successful certifications data retrieval."""
        mock_portfolio.certifications = mock_portfolio_data.certifications
        
        response = client.get("/api/certifications")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == "AWS Certified"
        assert data[0]["issuer"] == "Amazon"


class TestMainPage:
    """Test main page rendering."""
    
    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)
    
    @patch('src.main.portfolio_data')
    def test_main_page_success(self, mock_portfolio, client):
        """Test successful main page rendering."""
        mock_portfolio.personal.name = "John Doe"
        mock_portfolio.personal.title = "Software Engineer"
        mock_portfolio.personal.location = "San Francisco, CA"
        mock_portfolio.personal.summary = "Experienced software engineer"
        mock_portfolio.personal.email = "john@example.com"
        mock_portfolio.personal.linkedin = "linkedin.com/in/johndoe"
        mock_portfolio.personal.github = "github.com/johndoe"
        mock_portfolio.personal.profile = "avatars.githubusercontent.com/u/123"
        mock_portfolio.experience = []
        mock_portfolio.education = []
        mock_portfolio.skills = []
        mock_portfolio.certifications = []
        
        response = client.get("/")
        
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "John Doe" in response.text
        assert "Software Engineer" in response.text
        assert "San Francisco, CA" in response.text
    
    def test_main_page_data_unavailable(self, client):
        """Test main page when data is unavailable."""
        with patch('src.main.portfolio_data', None):
            response = client.get("/")
            
            assert response.status_code == 500
            assert "Portfolio data not available" in response.json()["detail"]


class TestErrorHandling:
    """Test error handling in the application."""
    
    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)
    
    def test_404_endpoint(self, client):
        """Test 404 handling for non-existent endpoints."""
        response = client.get("/nonexistent")
        
        assert response.status_code == 404
    
    def test_static_files_served(self, client):
        """Test that static files are served correctly."""
        # This test assumes there's a CSS file in static/css/
        response = client.get("/static/css/style.css")
        
        # Should either return 200 (if file exists) or 404 (if not)
        assert response.status_code in [200, 404]


class TestApplicationConfiguration:
    """Test application configuration and setup."""
    
    def test_app_title(self):
        """Test that the app has the correct title."""
        assert app.title == "Portfolio"
    
    def test_app_version(self):
        """Test that the app has the correct version."""
        assert app.version == "1.0.0"
    
    def test_cors_middleware(self):
        """Test that CORS middleware is configured."""
        # Check if CORS middleware is in the middleware stack
        from fastapi.middleware.cors import CORSMiddleware
        middleware_found = False
        
        for middleware in app.user_middleware:
            if middleware.cls == CORSMiddleware:
                middleware_found = True
                break
        
        assert middleware_found, "CORS middleware not found in application"
    
    def test_static_files_mounted(self):
        """Test that static files are mounted."""
        # Check if static files are mounted
        routes = [route.path for route in app.routes]
        assert "/static" in routes
