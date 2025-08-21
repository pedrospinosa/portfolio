# Deployment Configuration

## GitHub Pages Deployment

This project uses GitHub Actions to automatically deploy to GitHub Pages. The deployment requires a GitHub token for authentication.

### Required Secrets

#### `GENERAL_GITHUB_PAGES_TOKEN`

This secret is required for the GitHub Pages deployment workflow.

**How to create and configure:**

1. **Generate a Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Give it a descriptive name (e.g., "Portfolio GitHub Pages Token")
   - Select scopes:
     - `repo` (Full control of private repositories)
     - `workflow` (Update GitHub Action workflows)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again)

2. **Add the secret to your repository:**
   - Go to your repository on GitHub
   - Click Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GENERAL_GITHUB_PAGES_TOKEN`
   - Value: Paste the token you copied
   - Click "Add secret"

### Deployment Workflow

The deployment process:

1. **Quality Gates**: PR workflow runs all checks (tests, linting, type checking, security)
2. **Deployment Trigger**: If all checks pass, deploy workflow automatically triggers
3. **Build**: FastAPI app runs and generates static HTML
4. **Deploy**: Content is deployed to GitHub Pages

### Manual Deployment

You can also trigger deployment manually:

1. Go to your repository on GitHub
2. Click Actions tab
3. Select "Deploy Portfolio to GitHub Pages" workflow
4. Click "Run workflow" → "Run workflow"

### Troubleshooting

**If deployment fails:**

1. Check that `GENERAL_GITHUB_PAGES_TOKEN` is properly configured
2. Verify the token has the correct permissions
3. Check the Actions tab for detailed error messages
4. Ensure all quality checks pass before deployment

**Token Permissions:**
- The token needs `repo` scope for repository access
- The token needs `workflow` scope for GitHub Actions
- The repository needs GitHub Pages enabled in Settings → Pages
