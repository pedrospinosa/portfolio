import builtins
from io import StringIO

from src.data import load_portfolio_data


def test_skills_sorted_by_category_frequency(monkeypatch):
    yaml_content = """
personal:
  name: "John Doe"
  title: "Software Engineer"
  location: "City"
  summary: "Summary"
  email: "john@example.com"
  linkedin: "linkedin.com/in/johndoe"
  github: "github.com/johndoe"
  profile: "avatars.githubusercontent.com/u/123"
experience: []
education: []
skills:
  - category: "Programming"
    values:
      - "Python"
      - "Rust"
  - category: "Cloud"
    values:
      - "AWS"
      - "GCP"
  - category: "Backend"
    values:
      - "FastAPI"
certifications: []
"""

    def mock_open(*args, **kwargs):
        return StringIO(yaml_content)

    # Reset cache and mock file reading
    import src.data as data_module

    data_module._portfolio_data = None
    monkeypatch.setattr(builtins, "open", mock_open)

    portfolio = load_portfolio_data(use_cache=False)

    # Expect order by category frequency desc, then name asc
    # Cloud (2): AWS, GCP; Programming (2): Python, Rust; Backend (1): FastAPI
    expected_order = ["AWS", "GCP", "Python", "Rust", "FastAPI"]
    actual_order = [s.name for s in portfolio.skills]
    assert actual_order == expected_order


def test_skills_sorted_with_priority_over_count(monkeypatch):
    yaml_content = """
personal:
  name: "John Doe"
  title: "Software Engineer"
  location: "City"
  summary: "Summary"
  email: "john@example.com"
  linkedin: "linkedin.com/in/johndoe"
  github: "github.com/johndoe"
  profile: "avatars.githubusercontent.com/u/123"
experience: []
education: []
skills:
  - category: "A"
    values:
      - "A1"
      - "A2"
      - "A3"
      - "A4"
  - category: "B"
    priority: 0
    values:
      - "B1"
certifications: []
"""

    def mock_open(*args, **kwargs):
        return StringIO(yaml_content)

    import src.data as data_module

    data_module._portfolio_data = None
    monkeypatch.setattr(builtins, "open", mock_open)

    portfolio = load_portfolio_data(use_cache=False)

    categories_in_order: list[str] = []
    for skill in portfolio.skills:
        if not categories_in_order or categories_in_order[-1] != skill.category:
            categories_in_order.append(skill.category)

    assert categories_in_order[0] == "B"
