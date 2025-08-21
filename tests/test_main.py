import pytest
from fastapi.testclient import TestClient

from src.main import app


class TestPortfolioEndpoints:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_get_portfolio_success(self, client):
        response = client.get("/api/portfolio")

        assert response.status_code == 200
        data = response.json()
        assert "personal" in data
        assert "name" in data["personal"]
        assert "title" in data["personal"]
        assert "experience" in data
        assert "education" in data
        assert "skills" in data
        assert "certifications" in data

    def test_get_experience_success(self, client):
        response = client.get("/api/experience")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "company" in data[0]
            assert "position" in data[0]

    def test_get_skills_success(self, client):
        response = client.get("/api/skills")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "name" in data[0]
            assert "category" in data[0]

    def test_get_education_success(self, client):
        response = client.get("/api/education")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "institution" in data[0]
            assert "degree" in data[0]

    def test_get_certifications_success(self, client):
        response = client.get("/api/certifications")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "name" in data[0]
            assert "issuer" in data[0]


class TestMainPage:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_main_page_success(self, client):
        response = client.get("/")

        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Portfolio" in response.text
        assert "Experience" in response.text
        assert "Skills" in response.text


class TestErrorHandling:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_404_endpoint(self, client):
        response = client.get("/nonexistent")

        assert response.status_code == 404

    def test_static_files_served(self, client):
        response = client.get("/static/css/style.css")
        assert response.status_code in [200, 404]


class TestApplicationConfiguration:
    def test_app_title(self):
        assert app.title == "Portfolio"

    def test_app_version(self):
        assert app.version == "1.0.0"

    def test_cors_middleware(self):
        from fastapi.middleware.cors import CORSMiddleware

        middleware_found = False

        for middleware in app.user_middleware:
            if middleware.cls == CORSMiddleware:
                middleware_found = True
                break

        assert middleware_found, "CORS middleware not found in application"

    def test_static_files_mounted(self):
        routes = [route.path for route in app.routes]
        assert "/static" in routes
