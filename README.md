# Dental Content CrewAI Pipeline

## Overview
This project generates dental content using a modular CrewAI pipeline. Each agent is responsible for a single task, and the system is designed for extensibility and integration with FastAPI and Next.js.

## Getting Started

### Agent Management
Backend now supports agent management endpoints:
- `/agents` — List agents and their status
- `/agents/{agent_name}/enable` — Enable agent
- `/agents/{agent_name}/disable` — Disable agent
- `/agents/{agent_name}` — Get agent status

Frontend UI dynamically renders agent selection checkboxes, includes accessibility features (ARIA, keyboard navigation, screen reader support), loading/error feedback, and syncs with backend agent status.
See DEV_RULES.md for development workflow, versioning, and git rules.

## Features
- Modular agent-based content generation
- FastAPI backend
- Next.js frontend with accessible, scalable agent selection UI
- Dynamic agent management (enable/disable agents from frontend)
- Easily extensible with new agents (SEO, analytics, video, carousel, writer, visual)

## Setup
1. Clone the repo
2. Install backend dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run the API server:
	```bash
	uvicorn main:app --reload
	```
4. Scaffold and start the Next.js frontend:
	```bash
	npx create-next-app@latest frontend
	cd frontend
	npm install axios
	npm run dev
	```
5. The frontend will be available at http://localhost:3000 and will connect to the FastAPI backend at http://localhost:8000.

## Testing
1. Install test dependencies:
	 ```bash
	 pip install pytest
	 ```
2. Run tests:
	 ```bash
	 pytest
	 ```
See TESTING.md for more details.

## Deployment
For production:
- Use a process manager (e.g., gunicorn, uvicorn with --workers)
- Optionally, Dockerize the app for cloud deployment

### Docker Deployment
1. Build the Docker image:
	```bash
	docker build -t dental-content-backend .
	```
2. Run the container:
	```bash
	docker run -d -p 8000:8000 dental-content-backend
	```
3. The backend will be available at http://localhost:8000

For frontend, deploy using Vercel, Netlify, or your preferred platform. See frontend/README.md for details.

## API Usage

### Example: Generate Monthly Content
Request:
```json
{
	"topic": "Dental Implants",
	"posts_per_month": 6,
	"include_seo": true,
	"include_analytics": true,
	"include_video": false,
	"include_carousel": true
}
```
Response:
```json
{
	"monthly_content": [
		{
			"topic": "Dental implant vs bridge",
			"category": "comparison",
			"tone": "informative",
			"content": {"instagram": "...", "facebook": "...", ...},
			"visuals": {"image_prompt": "...", "reel_script": "..."},
			"seo": {"keywords": ["Dental implant", ...], "meta_description": "...", "title": "..."},
			"analytics": {"views": "...", "engagement": "...", "shares": "...", "tone": "..."},
			"carousel": {"slides": ["Slide 1: ...", "Slide 2: ..."], "meta": {"total_slides": 2, "tone": "informative", "topic": "Dental implant vs bridge"}}
		}
	]
}
```

### Example: Frontend Workflow
1. Enter a topic (e.g., "Dental Implants") and number of posts per month.
2. Select desired agents using checkboxes (SEO, analytics, video, carousel).
3. Click "Generate Content".
4. Agent outputs (SEO, analytics, video, carousel, visuals) will appear under each content item.

### Example: CRUD Operations
Create:
```json
{
	"topic": "Test Topic",
	"category": "Test Category",
	"tone": "Test Tone",
	"content": "Test Content",
	"visuals": "Test Visuals",
	"seo": "SEO output",
	"analytics": "Analytics output",
	"video": "Video output",
	"carousel": "Carousel output"
}
```
Get:
```json
{
	"id": 1,
	"topic": "Test Topic",
	"category": "Test Category",
	"tone": "Test Tone",
	"content": "Test Content",
	"visuals": "Test Visuals",
	"seo": "SEO output",
	"analytics": "Analytics output",
	"video": "Video output",
	"carousel": "Carousel output"
}
```

### Generate Monthly Content
**POST** `/generate/month`

**Request Body:**
```json
{
	"topic": "Invisalign",
	"posts_per_month": 12,
	"include_seo": true,
	"include_analytics": true,
	"include_video": true,
	"include_carousel": true
}
```

**Response:**
```json
{
	"monthly_content": [
		{
			"topic": "Invisalign vs braces",
			"category": "comparison",
			"tone": "informative",
			"content": {"instagram": "...", "facebook": "...", ...},
			"visuals": {"image_prompt": "...", "reel_script": "..."},
			"seo": {"keywords": ["Invisalign", ...], "meta_description": "...", "title": "..."},
			"analytics": {"views": "...", "engagement": "...", "shares": "...", "tone": "..."},
			"video": {"video_script": "...", "video_meta": "..."},
			"carousel": {"slides": [...], "meta": {"total_slides": 4, "tone": "...", "topic": "..."}}
		},
		...
	]
}
```

**Error Handling:**
- Invalid payload returns HTTP 422 with error details
- Unknown agent returns HTTP 404 with error message

### Content CRUD Endpoints

- **POST** `/content` — Create a content item
- **GET** `/content/{item_id}` — Retrieve a content item
- **PUT** `/content/{item_id}` — Update a content item
- **DELETE** `/content/{item_id}` — Delete a content item

**Example Create Request:**
```json
{
	"topic": "Test Topic",
	"category": "Test Category",
	"tone": "Test Tone",
	"content": "Test Content",
	"visuals": "Test Visuals",
	"seo": "SEO output (optional)",
	"analytics": "Analytics output (optional)",
	"video": "Video output (optional)",
	"carousel": "Carousel output (optional)"
}
```

**Example Response:**
```json
{
	"id": 1,
	"topic": "Test Topic"
}
```

**Example Get Response:**
```json
{
	"id": 1,
	"topic": "Test Topic",
	"category": "Test Category",
	"tone": "Test Tone",
	"content": "Test Content",
	"visuals": "Test Visuals",
	"seo": "SEO output",
	"analytics": "Analytics output",
	"video": "Video output",
	"carousel": "Carousel output"
}
```

**Error Handling:**
- Invalid ID returns HTTP 404 with error message
- Missing required fields returns HTTP 422

## Database Integration
- Uses SQLite via SQLAlchemy for persistent storage
- Content items are saved automatically when generated
- Alembic recommended for migrations

## Testing
- All core logic and CRUD endpoints covered by unit tests in `tests/`
- Run `pytest` to verify functionality

## Agents & Pipeline
- **Topic Agent:** Generates subtopics from a raw topic
- **Strategy Agent:** Assigns category and tone to each topic
- **Research Agent:** Gathers key points for each topic
- **Writer Agent:** Produces written content
- **Formatter Agent:** Formats content for each platform
- **Visual Agent:** Suggests visuals and scripts
- **SEO Agent:** Optimizes content for search engines
- **Analytics Agent:** Provides content performance insights
- **Video Agent:** Generates video content
- **Carousel Agent:** Creates carousel visual content

## Getting Started
Frontend UI dynamically renders agent selection checkboxes, includes accessibility features (ARIA, keyboard navigation, screen reader support), loading/error feedback, and syncs with backend agent status.

## Folder Structure
See ARCHITECTURE.md for details on modules and data flow.
