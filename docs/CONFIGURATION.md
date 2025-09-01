# Portfolio Configuration Guide

This guide explains how to configure your portfolio using the `portfolio.yml` file.

## Portfolio.yml Configuration

The `portfolio.yml` file contains all your portfolio data in YAML format. This file is loaded by the FastAPI application and rendered on your portfolio website.

### File Location

```
portfolio/
├── src/
├── templates/
├── portfolio.yml  ← Edit this file with your information
└── ...
```

### Configuration Structure

```yaml
personal:
  name: "Your Name"
  title: "Your Professional Title"
  location: "Your Location"
  summary: "Your professional summary..."
  email: "your.email@example.com"
  linkedin: "linkedin.com/in/yourprofile"
  github: "github.com/yourusername"
  profile: "avatars.githubusercontent.com/u/yourid"

experience:
  - company: "Company Name"
    position: "Your Position"
    duration: "Duration"
    location: "Location"
    period: "Period"
    achievements:
      - "Achievement 1"
      - "Achievement 2"

education:
  - institution: "University Name"
    degree: "Degree Name"
    period: "Period"
    location: "Location"

skills:
  - name: "Skill Name"
    category: "Category"

certifications:
  - name: "Certification Name"
    issuer: "Issuing Organization"
```

## Detailed Configuration

### Personal Information

```yaml
personal:
  name: "John Doe"                    # Your full name
  title: "Software Engineer"          # Your professional title
  location: "San Francisco, CA"       # Your location
  summary: |
    Your professional summary here.
    You can use multiple lines.
    This will be displayed on your portfolio.
  email: "john.doe@example.com"       # Your email address
  linkedin: "linkedin.com/in/johndoe" # Your LinkedIn profile
  github: "github.com/johndoe"        # Your GitHub profile
  profile: "avatars.githubusercontent.com/u/123" # GitHub avatar URL
```

**Required fields:** All fields are required.

### Experience

```yaml
experience:
  - company: "Tech Company Inc."
    position: "Senior Software Engineer"
    duration: "2 years 6 months"
    location: "San Francisco, CA"
    period: "January 2022 - June 2024"
    achievements:
      - "Led development of scalable microservices architecture"
      - "Improved system performance by 40%"
      - "Mentored 3 junior developers"
```

**Required fields:** All fields are required.

**Achievements:** List your key accomplishments and contributions.

### Education

```yaml
education:
  - institution: "University of Technology"
    degree: "Bachelor of Science in Computer Science"
    period: "2018 - 2022"
    location: "San Francisco, CA"
```

**Required fields:** All fields are required.

### Skills (grouped format)

```yaml
skills:
  - category: "AI/ML"
    priority: 0            # optional; lower is higher, omit = lowest
    values:
      - "Machine Learning"
      - "Deep Learning"

  - category: "DevOps"
    priority: 1
    values:
      - "Docker"
      - "Kubernetes"

  - category: "Programming Languages"
    values:
      - "Python"
      - "Go"
```

- `category` and `values` are required.
- `priority` is optional (integer). Lower numbers are shown first; omitted = lowest.

### Certifications

```yaml
certifications:
  - name: "AWS Certified Solutions Architect"
    issuer: "Amazon Web Services"
  - name: "Google Cloud Professional Developer"
    issuer: "Google"
```

**Required fields:** Both `name` and `issuer` are required.

## Validation

The application validates your `portfolio.yml` file using Pydantic models. If there are any issues:

1. **Missing fields:** All required fields must be present
2. **Invalid format:** Ensure proper YAML syntax
3. **Type errors:** Check that data types match expected format

### Common Validation Errors

- **Missing required field:** Add the missing field
- **Invalid email format:** Use a valid email address
- **Invalid URL format:** Ensure LinkedIn and GitHub URLs are valid
- **Empty lists:** If you have no experience/education/skills/certifications, use empty lists `[]`

## Example Configuration

See the current `portfolio.yml` file in the project root for a complete example.

## Customization Tips

1. **Professional Summary:** Write a compelling summary that highlights your expertise
2. **Achievements:** Use action verbs and quantify results when possible
3. **Skills Organization:** Group related skills together for better presentation
4. **Consistent Formatting:** Maintain consistent date formats and location formats

## Testing Your Configuration

After updating `portfolio.yml`:

1. **Run locally:** `uv run dev` to test your changes
2. **Check validation:** The application will show errors if configuration is invalid
3. **Preview:** Visit `http://localhost:8000` to see your portfolio

## Deployment

Once your configuration is complete:

1. Commit your changes: `git add portfolio.yml && git commit -m "Update portfolio data"`
2. Push to main branch: `git push origin main`
3. The CI/CD pipeline will automatically deploy your updated portfolio

## Support

If you encounter issues with your configuration:

1. Check the validation errors in the application logs
2. Verify YAML syntax using an online YAML validator
3. Compare with the example configuration in the project
4. Check the [main README](../README.md) for additional setup instructions
