# Dental Content CrewAI Pipeline

## Overview
This project generates dental content using a modular CrewAI pipeline. Each agent is responsible for a single task, and the system is designed for extensibility and integration with FastAPI and Next.js.

## Features
- Modular agent-based content generation
- FastAPI backend
- Ready for Next.js frontend integration
- Easily extensible with new agents (SEO, analytics, etc.)

## Setup
1. Clone the repo
2. Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```
3. Run the API server:
	 ```bash
	 uvicorn main:app --reload
	 ```

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
- For production, use a process manager (e.g., gunicorn, uvicorn with --workers)
- Optionally, Dockerize the app for cloud deployment

## API Usage

### Generate Monthly Content
**POST** `/generate/month`

**Request Body:**
```json
{
	"topic": "Invisalign",
	"posts_per_month": 12
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
			"visuals": {"image_prompt": "...", "reel_script": "..."}
		},
		...
	]
}
```

## Agents & Pipeline
- **Topic Agent:** Generates subtopics from a raw topic
- **Strategy Agent:** Assigns category and tone to each topic
- **Research Agent:** Gathers key points for each topic
- **Writer Agent:** Produces written content
- **Formatter Agent:** Formats content for each platform
- **Visual Agent:** Suggests visuals and scripts

## Folder Structure
See ARCHITECTURE.md for details on modules and data flow.
