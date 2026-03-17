# Testing Guide

## Running Tests

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```
2. Run all tests:
   ```bash
   pytest
   ```

## Test Coverage
- Each agent has a dedicated test file in `tests/`
- Add new tests for any new agent or pipeline

### Agent Selection & Content Generation
- `tests/test_generate_month_endpoint.py`: Backend tests for `/generate/month` endpoint with all agent combinations and error handling.
- `frontend/__tests__/index.test.js`: Frontend tests for agent selection UI, output display, and error popup.

#### Scenarios
1. Backend: All combinations of agent selection (SEO, analytics, video, carousel, none, all).
2. Backend: Invalid payload returns 422 error.
3. Frontend: User selects agents, generates content, sees correct outputs.
4. Frontend: Error popup shown if backend fails.
