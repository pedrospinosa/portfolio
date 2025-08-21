# Portfolio Development Milestones

This document outlines the planned development milestones for the portfolio project.

## 🎯 **Milestone Overview**

### **M0: Refactor main to move routes to views.py**
- **Goal**: Separate routing logic from application setup
- **Benefits**: Better code organization, easier testing, cleaner main.py

### **M1: Setup pre-commit, mypy, ruff**
- **Goal**: Add code quality tools and automated checks
- **Benefits**: Consistent code style, type safety, catch issues early

### **M2: Configure PR workflow and make deploy depend on tests**
- **Goal**: Ensure quality gates before deployment
- **Benefits**: Prevent broken code from being deployed, automated quality checks

---

## **M0: Refactor Routes to views.py**

### **Objective**
Separate routing logic from application setup to improve code organization and maintainability.

### **Implementation Plan**

**New Structure:**
```
src/
├── main.py          # App setup, middleware, startup
├── views.py         # All route handlers
└── data.py          # Data loading (existing)
```

**Tasks:**
- [ ] Create `src/views.py` with all route handlers
- [ ] Move route functions from `main.py` to `views.py`
- [ ] Update `main.py` to import and register routes
- [ ] Update tests to reflect new structure
- [ ] Ensure all functionality works as before

**Benefits:**
- ✅ **Separation of concerns**: App config vs route logic
- ✅ **Easier testing**: Mock views independently
- ✅ **Cleaner main.py**: Focus on app setup
- ✅ **Better organization**: Routes grouped logically

---

## **M1: Code Quality Tools**

### **Objective**
Add automated code quality checks and formatting tools to ensure consistent, high-quality code.

### **Tools to Implement**

**pre-commit**
- Git hooks for automated checks
- Run before each commit
- Prevent bad code from being committed

**mypy**
- Static type checking
- Catch type errors early
- Improve code reliability

**ruff**
- Fast Python linter and formatter
- Consistent code style
- Replace multiple tools (flake8, black, isort)

### **Implementation Plan**

**Tasks:**
- [ ] Add pre-commit configuration
- [ ] Configure mypy for type checking
- [ ] Setup ruff for linting and formatting
- [ ] Add development dependencies
- [ ] Create pre-commit hooks
- [ ] Update documentation

**Benefits:**
- ✅ **Consistent code style**: Automatic formatting
- ✅ **Type safety**: Catch type errors early
- ✅ **Quality gates**: Prevent bad code from being committed
- ✅ **Developer experience**: Fast feedback

---

## **M2: CI/CD Workflow**

### **Objective**
Implement proper CI/CD pipeline with quality gates to ensure only tested, quality code gets deployed.

### **Workflow Structure**

**New Structure:**
```
.github/workflows/
├── pr.yml          # PR checks (tests, linting, type checking)
└── deploy.yml      # Deployment (depends on PR checks)
```

### **Implementation Plan**

**PR Workflow (`pr.yml`):**
- [x] Run unit tests
- [x] Run linting checks (ruff)
- [x] Run type checking (mypy)
- [x] Run pre-commit checks
- [x] Run security checks (bandit)
- [x] Test API endpoints
- [x] Ensure all checks pass

**Deploy Workflow (`deploy.yml`):**
- [x] Depend on PR workflow success
- [x] Deploy to production
- [x] Only trigger on main branch
- [x] Include deployment status

**Tasks:**
- [x] Create `pr.yml` workflow
- [x] Update `deploy.yml` to depend on PR checks
- [x] Configure branch protection rules
- [x] Test workflow integration
- [x] Update documentation

**Benefits:**
- ✅ **Quality gates**: Tests must pass before deploy
- ✅ **Automated checks**: No manual verification needed
- ✅ **Faster feedback**: Issues caught in PR, not after deploy
- ✅ **Reliable deployments**: Only tested code gets deployed

---

## **Implementation Order**

**Recommended Order:**
1. **M0** - Refactor routes (foundation)
2. **M1** - Code quality tools (quality)
3. **M2** - CI/CD workflow (automation)

**Rationale:**
- M0 provides clean architecture foundation
- M1 adds quality tools to the clean structure
- M2 automates quality checks in CI/CD

---

## **Success Criteria**

### **M0 Success:**
- [ ] All routes moved to `views.py`
- [ ] `main.py` only handles app setup
- [ ] All tests pass
- [ ] No functionality regression

### **M1 Success:**
- [ ] pre-commit hooks working
- [ ] mypy type checking passing
- [ ] ruff linting and formatting working
- [ ] Code style consistent across project

### **M2 Success:**
- [x] PR workflow runs on all PRs
- [x] Deploy only happens after PR checks pass
- [x] All quality gates enforced
- [x] Automated deployment working

---

## **Notes**

- Each milestone should be completed and tested before moving to the next
- All changes should maintain backward compatibility
- Documentation should be updated for each milestone
- Tests should be updated to reflect new structure
