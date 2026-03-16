from fastapi import APIRouter
from content_factory.pipelines.monthly_content_pipeline import generate_monthly_content
from pydantic import BaseModel
from typing import Any, Dict, List

router = APIRouter()

class TopicRequest(BaseModel):
    topic: str
    posts_per_month: int = 12

@router.post(
    "/generate/month",
    tags=["Content Generation"],
    summary="Generate a monthly content plan",
    response_description="A list of generated content items for the month."
)
def generate_monthly(request: TopicRequest) -> Dict[str, List[Dict[str, Any]]]:
    """
    Generate a monthly content plan for a given topic.
    - **topic**: The main topic to generate content for (e.g., 'Invisalign')
    - **posts_per_month**: Number of posts to generate (default: 12)
    Returns a list of content items, each with topic, category, tone, content, and visuals.
    """
    content = generate_monthly_content(request.topic, request.posts_per_month)
    return {"monthly_content": content}
