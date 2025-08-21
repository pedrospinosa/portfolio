import pytest
import yaml
from pydantic import ValidationError

from src.data import (
    Experience,
    PersonalInfo,
    PortfolioData,
    Skill,
    load_portfolio_data,
)


class TestPortfolioDataModels:
    def test_personal_info_model(self):
        valid_data = {
            "name": "John Doe",
            "title": "Software Engineer",
            "location": "San Francisco, CA",
            "summary": "Experienced software engineer",
            "email": "john@example.com",
            "linkedin": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe",
            "profile": "avatars.githubusercontent.com/u/123",
        }

        personal_info = PersonalInfo(**valid_data)
        assert personal_info.name == "John Doe"
        assert personal_info.email == "john@example.com"

    def test_experience_model(self):
        valid_data = {
            "company": "Tech Corp",
            "position": "Senior Engineer",
            "duration": "2 years",
            "location": "San Francisco, CA",
            "period": "2022-2024",
            "achievements": ["Built scalable system", "Led team of 5"],
        }

        experience = Experience(**valid_data)
        assert experience.company == "Tech Corp"
        assert len(experience.achievements) == 2

    def test_skill_model(self):
        valid_data = {"name": "Python", "category": "Programming"}

        skill = Skill(**valid_data)
        assert skill.name == "Python"
        assert skill.category == "Programming"

    def test_portfolio_data_model(self):
        valid_data = {
            "personal": {
                "name": "John Doe",
                "title": "Software Engineer",
                "location": "San Francisco, CA",
                "summary": "Experienced software engineer",
                "email": "john@example.com",
                "linkedin": "linkedin.com/in/johndoe",
                "github": "github.com/johndoe",
                "profile": "avatars.githubusercontent.com/u/123",
            },
            "experience": [
                {
                    "company": "Tech Corp",
                    "position": "Senior Engineer",
                    "duration": "2 years",
                    "location": "San Francisco, CA",
                    "period": "2022-2024",
                    "achievements": ["Built scalable system"],
                }
            ],
            "education": [
                {
                    "institution": "University of Tech",
                    "degree": "Computer Science",
                    "period": "2018-2022",
                    "location": "San Francisco, CA",
                }
            ],
            "skills": [{"name": "Python", "category": "Programming"}],
            "certifications": [{"name": "AWS Certified", "issuer": "Amazon"}],
        }

        portfolio = PortfolioData(**valid_data)
        assert portfolio.personal.name == "John Doe"
        assert len(portfolio.experience) == 1
        assert len(portfolio.education) == 1
        assert len(portfolio.skills) == 1
        assert len(portfolio.certifications) == 1


class TestDataLoading:
    def test_load_valid_yaml(self):
        test_file = "tests/resources/test_portfolio.yml"
        portfolio_data = load_portfolio_data(test_file, use_cache=False)

        assert portfolio_data.personal.name == "John Doe"
        assert portfolio_data.personal.email == "john.doe@example.com"
        assert portfolio_data.personal.title == "Software Engineer"
        assert len(portfolio_data.experience) == 2
        assert len(portfolio_data.education) == 1
        assert len(portfolio_data.skills) == 6
        assert len(portfolio_data.certifications) == 2

    def test_load_invalid_yaml(self):
        test_file = "tests/resources/invalid_portfolio.yml"

        with pytest.raises(ValidationError):
            load_portfolio_data(test_file, use_cache=False)

    def test_load_missing_file(self):
        with pytest.raises(FileNotFoundError):
            load_portfolio_data("/path/to/nonexistent.yml", use_cache=False)

    def test_load_malformed_yaml(self):
        test_file = "tests/resources/malformed_portfolio.yml"

        with pytest.raises((yaml.YAMLError, ValueError)):
            load_portfolio_data(test_file, use_cache=False)


class TestCaching:
    def test_caching_behavior(self, monkeypatch):
        call_count = 0

        def mock_open(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            yaml_content = """personal:
  name: "Cache Test User"
  title: "Test Engineer"
  location: "Test City"
  summary: "Test summary for caching"
  email: "cache@test.com"
  linkedin: "linkedin.com/in/cachetest"
  github: "github.com/cachetest"
  profile: "avatars.githubusercontent.com/u/cache123"
experience: []
education: []
skills: []
certifications: []"""

            from io import StringIO

            return StringIO(yaml_content)

        monkeypatch.setattr("builtins.open", mock_open)

        import src.data

        src.data._portfolio_data = None

        result1 = load_portfolio_data()
        assert call_count == 1
        assert result1.personal.name == "Cache Test User"

        result2 = load_portfolio_data()
        assert call_count == 1
        assert result1 is result2


class TestErrorHandling:
    def test_load_portfolio_data_with_error(self, monkeypatch):
        def mock_open(*args, **kwargs):
            raise FileNotFoundError("Test error")

        monkeypatch.setattr("builtins.open", mock_open)

        with pytest.raises(FileNotFoundError, match="Test error"):
            load_portfolio_data(use_cache=False)
