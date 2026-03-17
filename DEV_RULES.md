## Development Rules & Workflow

### 1. Branching & Versioning
- Use `main` for production-ready code.
- Create feature branches for new features or fixes.
- Commit only working, tested code.
- Tag releases with semantic versioning (e.g., v1.0.0).

### 2. Code Quality
- Follow PEP8 for Python and Airbnb/Prettier for JS/TS.
- Use descriptive commit messages.
- Run tests before merging.
- Document all new features in README.

### 3. Testing
- Backend: Use pytest for all API and agent logic.
- Frontend: Use Jest and React Testing Library.
- Add tests for new features and bug fixes.

### 4. Documentation
- Update README.md and DEV_RULES.md for all major changes.
- Add screenshots and usage examples.
- Document API endpoints and agent selection logic.

### 5. Git Workflow
- Commit frequently, push often.
- Use pull requests for review.
- Reference issues/feature requests in commits.

### 6. Deployment
- Deploy frontend on Vercel, backend on preferred cloud.
- Ensure .env files are not committed.

---
For more details, see README.md and TESTING.md.
