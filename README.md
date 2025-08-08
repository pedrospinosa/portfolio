# Pedro Spinosa - Portfolio

A modern, responsive portfolio website showcasing my experience as an ML Engineer at Nubank and expertise in AI/ML, MLOps, and infrastructure.

## 🌐 Live Portfolio Deployment

Visit the portfolio at: [https://pedrospinosa.dev](https://pedrospinosa.dev)

## ✨ Features

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
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)
- **Deployment**: GitHub Pages, Docker support

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
   uv run uvicorn src.main:app --reload --host 127.0.0.1 --port 8080
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:8080`

## 🏗️ Project Structure

```
portfolio/
├── src/
│   ├── __init__.py
│   └── main.py            # FastAPI application
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   ├── js/
│   │   └── main.js        # JavaScript functionality
│   └── images/            # Static images
├── pyproject.toml         # Project configuration
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
└── README.md              # This file
```

## 🌐 API Endpoints

- `GET /` - Main portfolio page
- `GET /api/portfolio` - Complete portfolio data (JSON)
- `GET /api/experience` - Work experience data
- `GET /api/skills` - Skills and expertise
- `GET /api/education` - Education information
- `GET /api/certifications` - Certifications

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

### Using Docker directly

```bash
docker build -t portfolio .
docker run -p 8000:8000 portfolio
```

## 📦 Deployment Options

### GitHub Pages (Static)

1. Push your code to GitHub
2. Enable GitHub Pages in repository settings
3. Set source to main branch
4. The GitHub Actions workflow will automatically deploy

### Production Deployment

- **Cloud Platforms**: Deploy to AWS, Google Cloud, or Azure
- **VPS**: Deploy to a virtual private server
- **Container Orchestration**: Use Kubernetes or Docker Swarm

## 🎨 Customization

### Updating Portfolio Data

Edit the `portfolio_data` object in `src/main.py`:

```python
portfolio_data = PortfolioData(
    name="Your Name",
    title="Your Title",
    location="Your Location",
    summary="Your summary..."
)
```

### Styling

Modify `static/css/style.css` to customize colors, fonts, and layout:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1f2937;
}
```

## 🔧 Development

### Adding New Features

1. **Backend**: Add new endpoints in `src/main.py`
2. **Frontend**: Update templates and static files
3. **Styling**: Modify CSS for new components

### Testing

```bash
# Run the application
uv run uvicorn src.main:app --reload

# Test API endpoints
curl http://localhost:8080/api/portfolio
```

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
- **Portfolio**: [https://pedrospinosa.dev](https://pedrospinosa.dev)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- uv for modern Python package management
- Font Awesome for beautiful icons
- Google Fonts for typography
