"""
Unit tests for the data loading module.
"""

import pytest
import tempfile
import os
from pathlib import Path
from pydantic import ValidationError

from src.data import (
    load_profile_data,
    get_portfolio_data,
    get_cached_portfolio_data,
    reload_portfolio_data,
    PortfolioData,
    PersonalInfo,
    Experience,
    Education,
    Skill,
    Certification
)


class TestPortfolioDataModels:
    """Test Pydantic models for portfolio data."""
    
    def test_personal_info_model(self):
        """Test PersonalInfo model validation."""
        valid_data = {
            "name": "John Doe",
            "title": "Software Engineer",
            "location": "San Francisco, CA",
            "summary": "Experienced software engineer",
            "email": "john@example.com",
            "linkedin": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe",
            "profile": "avatars.githubusercontent.com/u/123"
        }
        
        personal_info = PersonalInfo(**valid_data)
        assert personal_info.name == "John Doe"
        assert personal_info.email == "john@example.com"
    
    def test_experience_model(self):
        """Test Experience model validation."""
        valid_data = {
            "company": "Tech Corp",
            "position": "Senior Engineer",
            "duration": "2 years",
            "location": "San Francisco, CA",
            "period": "2022-2024",
            "achievements": ["Built scalable system", "Led team of 5"]
        }
        
        experience = Experience(**valid_data)
        assert experience.company == "Tech Corp"
        assert len(experience.achievements) == 2
    
    def test_skill_model(self):
        """Test Skill model validation."""
        valid_data = {
            "name": "Python",
            "category": "Programming"
        }
        
        skill = Skill(**valid_data)
        assert skill.name == "Python"
        assert skill.category == "Programming"
    
    def test_portfolio_data_model(self):
        """Test complete PortfolioData model validation."""
        valid_data = {
            "personal": {
                "name": "John Doe",
                "title": "Software Engineer",
                "location": "San Francisco, CA",
                "summary": "Experienced software engineer",
                "email": "john@example.com",
                "linkedin": "linkedin.com/in/johndoe",
                "github": "github.com/johndoe",
                "profile": "avatars.githubusercontent.com/u/123"
            },
            "experience": [
                {
                    "company": "Tech Corp",
                    "position": "Senior Engineer",
                    "duration": "2 years",
                    "location": "San Francisco, CA",
                    "period": "2022-2024",
                    "achievements": ["Built scalable system"]
                }
            ],
            "education": [
                {
                    "institution": "University of Tech",
                    "degree": "Computer Science",
                    "period": "2018-2022",
                    "location": "San Francisco, CA"
                }
            ],
            "skills": [
                {
                    "name": "Python",
                    "category": "Programming"
                }
            ],
            "certifications": [
                {
                    "name": "AWS Certified",
                    "issuer": "Amazon"
                }
            ]
        }
        
        portfolio = PortfolioData(**valid_data)
        assert portfolio.personal.name == "John Doe"
        assert len(portfolio.experience) == 1
        assert len(portfolio.education) == 1
        assert len(portfolio.skills) == 1
        assert len(portfolio.certifications) == 1


class TestDataLoading:
    """Test data loading functionality."""
    
    def test_load_valid_yaml(self):
        """Test loading valid YAML data."""
        yaml_content = """
personal:
  name: "John Doe"
  title: "Software Engineer"
  location: "San Francisco, CA"
  summary: "Experienced software engineer"
  email: "john@example.com"
  linkedin: "linkedin.com/in/johndoe"
  github: "github.com/johndoe"
  profile: "avatars.githubusercontent.com/u/123"
experience: []
education: []
skills: []
certifications: []
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write(yaml_content)
            temp_file = f.name
        
        try:
            portfolio_data = load_profile_data(temp_file)
            assert portfolio_data.personal.name == "John Doe"
            assert portfolio_data.personal.email == "john@example.com"
        finally:
            os.unlink(temp_file)
    
    def test_load_invalid_yaml(self):
        """Test loading invalid YAML data."""
        invalid_yaml = """
personal:
  name: "John Doe"
  # Missing required fields
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write(invalid_yaml)
            temp_file = f.name
        
        try:
            with pytest.raises(ValidationError):
                load_profile_data(temp_file)
        finally:
            os.unlink(temp_file)
    
    def test_load_missing_file(self):
        """Test loading non-existent file."""
        with pytest.raises(FileNotFoundError):
            load_profile_data("nonexistent.yml")
    
    def test_load_malformed_yaml(self):
        """Test loading malformed YAML."""
        malformed_yaml = """
personal:
  name: "John Doe"
  title: "Software Engineer"
  # Invalid YAML syntax
  location: "San Francisco, CA
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write(malformed_yaml)
            temp_file = f.name
        
        try:
            with pytest.raises(Exception):  # yaml.YAMLError
                load_profile_data(temp_file)
        finally:
            os.unlink(temp_file)


class TestCaching:
    """Test caching functionality."""
    
    def test_caching_behavior(self, monkeypatch):
        """Test that data is cached and not reloaded."""
        # Mock the load_profile_data function to track calls
        call_count = 0
        
        def mock_load_profile_data(profile_path=None):
            nonlocal call_count
            call_count += 1
            
            # Return a minimal valid portfolio
            return PortfolioData(
                personal=PersonalInfo(
                    name="Test User",
                    title="Test Title",
                    location="Test Location",
                    summary="Test summary",
                    email="test@example.com",
                    linkedin="linkedin.com/in/test",
                    github="github.com/test",
                    profile="avatars.githubusercontent.com/u/test"
                ),
                experience=[],
                education=[],
                skills=[],
                certifications=[]
            )
        
        # Patch the function
        monkeypatch.setattr("src.data.load_profile_data", mock_load_profile_data)
        
        # Reset the global cache
        import src.data
        src.data._portfolio_data = None
        
        # First call should load data
        result1 = get_cached_portfolio_data()
        assert call_count == 1
        assert result1.personal.name == "Test User"
        
        # Second call should use cache
        result2 = get_cached_portfolio_data()
        assert call_count == 1  # Should not increase
        assert result1 is result2  # Should be the same object
    
    def test_reload_functionality(self, monkeypatch):
        """Test that reload_portfolio_data forces a reload."""
        call_count = 0
        
        def mock_load_profile_data(profile_path=None):
            nonlocal call_count
            call_count += 1
            
            return PortfolioData(
                personal=PersonalInfo(
                    name=f"Test User {call_count}",
                    title="Test Title",
                    location="Test Location",
                    summary="Test summary",
                    email="test@example.com",
                    linkedin="linkedin.com/in/test",
                    github="github.com/test",
                    profile="avatars.githubusercontent.com/u/test"
                ),
                experience=[],
                education=[],
                skills=[],
                certifications=[]
            )
        
        # Patch the function
        monkeypatch.setattr("src.data.load_profile_data", mock_load_profile_data)
        
        # Reset the global cache
        import src.data
        src.data._portfolio_data = None
        
        # First call
        result1 = get_cached_portfolio_data()
        assert call_count == 1
        assert result1.personal.name == "Test User 1"
        
        # Reload should force a new load
        result2 = reload_portfolio_data()
        assert call_count == 2
        assert result2.personal.name == "Test User 2"
        assert result1 is not result2  # Should be different objects


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_get_portfolio_data_with_error(self, monkeypatch):
        """Test get_portfolio_data when loading fails."""
        def mock_load_profile_data(profile_path=None):
            raise FileNotFoundError("Test error")
        
        monkeypatch.setattr("src.data.load_profile_data", mock_load_profile_data)
        
        with pytest.raises(RuntimeError, match="Failed to load portfolio data"):
            get_portfolio_data()
    
    def test_get_cached_portfolio_data_with_error(self, monkeypatch):
        """Test get_cached_portfolio_data when loading fails."""
        def mock_get_portfolio_data():
            raise RuntimeError("Test error")
        
        monkeypatch.setattr("src.data.get_portfolio_data", mock_get_portfolio_data)
        
        # Reset the global cache
        import src.data
        src.data._portfolio_data = None
        
        with pytest.raises(RuntimeError, match="Test error"):
            get_cached_portfolio_data()
