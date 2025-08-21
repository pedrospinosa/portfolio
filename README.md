# Portfolio - A Forkable Portfolio Website

A modern, responsive portfolio website built with FastAPI and Jinja2. **Easily forkable** - just update the `portfolio.yml` file to customize your own portfolio!

## ✨ Features

- **Easy Customization**: All data stored in `portfolio.yml` - no Python code changes needed
- **Modern Design**: Clean, professional interface with smooth animations
- **Responsive Layout**: Perfect on desktop, tablet, and mobile devices
- **FastAPI Backend**: Modern Python web framework with API endpoints
- **Interactive Timeline**: Visual representation of work experience
- **Skills Organization**: Categorized skills and expertise
- **Contact Form**: Easy way for visitors to get in touch
- **SEO Optimized**: Ready for search engines

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11+
- **Package Manager**: uv (modern Python package manager)
- **Data**: YAML configuration with Pydantic validation
- **Code Quality**: ruff (linting & formatting), mypy (type checking), pre-commit (hooks)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 📋 Quick Start

### Prerequisites

- Python 3.11 or higher
- uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/spinosaphb/portfolio.git
   cd portfolio
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the development server**
   ```bash
   uv run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:8000`

## 🏗️ Project Structure

```
portfolio/
├── src/
│   ├── __init__.py
│   ├── main.py            # FastAPI application
│   └── data.py            # YAML data loading and validation
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   ├── js/
│   │   └── main.js        # JavaScript functionality
│   └── images/            # Static images
├── portfolio.yml          # Your portfolio data (edit this!)
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## 🌐 API Endpoints

- `GET /` - Main portfolio page
- `GET /api/portfolio` - Complete portfolio data (JSON)
- `GET /api/experience` - Work experience data
- `GET /api/skills` - Skills and expertise
- `GET /api/education` - Education information
- `GET /api/certifications` - Certifications

## 🚀 Quick Customization

### 1. Update Your Information

Edit `portfolio.yml` with your details:

```yaml
personal:
  name: "Your Name"
  title: "Your Title"
  location: "Your Location"
  summary: "Your professional summary..."
  email: "your.email@example.com"
  linkedin: "www.linkedin.com/in/yourprofile"
  github: "github.com/yourusername"
  profile: "avatars.githubusercontent.com/u/yourid"
```

### 2. Add Your Experience

```yaml
experience:
  - company: "Your Company"
    position: "Your Position"
    duration: "Duration"
    location: "Location"
    period: "Period"
    achievements:
      - "Your achievement 1"
      - "Your achievement 2"
```

### 3. Update Skills & Education

Add your skills, education, and certifications in the respective sections.

## 📦 Deployment Options

### Local Development

```bash
uv run dev  # Development with auto-reload
uv run start  # Production mode
```

### Production Deployment

- **Cloud Platforms**: Deploy to AWS, Google Cloud, or Azure
- **VPS**: Deploy to a virtual private server
- **Platform Services**: Render, Railway, Heroku, etc.

## 🎨 Customization

### Updating Portfolio Data

**No Python code changes needed!** Simply edit `portfolio.yml`:

```yaml
personal:
  name: "Your Name"
  title: "Your Title"
  location: "Your Location"
  summary: "Your summary..."
```

### Styling

Modify `static/css/style.css` to customize colors, fonts, and layout:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1f2937;
}
```

## 🧪 Testing

The project includes comprehensive unit tests to ensure reliability:

### Running Tests

```bash
# Run all tests
uv run test

# Run tests with verbose output
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_data.py -v

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html
```

## 🔧 Development

### Code Quality Tools

This project uses modern code quality tools:

```bash
# Install development dependencies
uv sync --extra dev

# Run linting and formatting
uv run ruff check .
uv run ruff format .

# Run type checking
uv run mypy src/

# Run all pre-commit hooks
uv run pre-commit run --all-files

# Install pre-commit hooks (run once)
uv run pre-commit install
```

### Adding New Features

1. **Backend**: Add new endpoints in `src/views.py`
2. **Frontend**: Update templates and static files
3. **Styling**: Modify CSS for new components
4. **Tests**: Add corresponding unit tests in `tests/`

### Testing

```bash
# Run the application
uv run dev

# Test API endpoints
curl http://localhost:8000/api/portfolio

# Run unit tests
uv run test

# Or run tests directly
python -m pytest tests/ -v
```

### Code Quality

The project enforces high code quality standards:

- **Ruff**: Fast Python linter and formatter
- **Mypy**: Static type checking
- **Pre-commit**: Git hooks for automated checks
- **100% Test Coverage**: Comprehensive unit tests

## 📱 Mobile Responsiveness

The portfolio is fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🎯 Performance Features

- **Lazy Loading**: Images and content load as needed
- **Smooth Animations**: CSS transitions and JavaScript animations
- **Optimized Assets**: Minified CSS and JavaScript
- **Fast Loading**: Optimized for quick page loads

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **Email**: spinosaphb@gmail.com
- **LinkedIn**: [Pedro Spinosa](https://www.linkedin.com/in/pedrospinosa)
- **GitHub**: [pedrospinosa](https://github.com/pedrospinosa)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- uv for modern Python package management
- Font Awesome for beautiful icons
- Google Fonts for typography
