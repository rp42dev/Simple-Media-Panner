from fastapi import APIRouter, Depends, HTTPException
import logging
from content_factory.pipelines.monthly_content_pipeline import generate_monthly_content
from content_factory.database.models import ContentItem, get_db, Base, engine
from pydantic import BaseModel, Field
from typing import Any, Dict, List
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("content_factory.api")
router = APIRouter()

# List all content items
@router.get(
    "/content",
    tags=["Content CRUD"],
    summary="List all content items",
    response_description="List of all content items"
)
def list_content_items(db: Session = Depends(get_db)):
    """
    List all content items.
    """
    items = db.query(ContentItem).all()
    return {"items": [
        {
            "id": item.id,
            "topic": item.topic,
            "category": item.category,
            "tone": item.tone,
            "content": item.content,
            "visuals": item.visuals,
            "seo": item.seo,
            "analytics": item.analytics,
            "video": item.video,
            "carousel": item.carousel,
            "formatted_content": item.formatted_content,
            "research_points": item.research_points,
            "strategy": item.strategy,
            "topics": item.topics,
            "visual_prompts": item.visual_prompts,
            "writer_output": item.writer_output
        } for item in items
    ]}
from fastapi import APIRouter, Depends, HTTPException
import logging
from content_factory.pipelines.monthly_content_pipeline import generate_monthly_content
from content_factory.database.models import ContentItem, get_db, Base, engine
from pydantic import BaseModel, Field
from typing import Any, Dict, List
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("content_factory.api")
router = APIRouter()
@router.get(
    "/agents",
    tags=["Agent Management"],
    summary="List available agents",
    response_description="List of agent names and status"
)
def list_agents():
    """
    List all available agents and their enabled status.
    """
    return {"agents": AGENTS}

@router.post(
    "/agents/{agent_name}/enable",
    tags=["Agent Management"],
    summary="Enable an agent",
    response_description="Agent enabled confirmation"
)
def enable_agent(agent_name: str):
    """
    Enable a specific agent.
    """
    if agent_name not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")
    AGENTS[agent_name]["enabled"] = True
    logger.info(f"Agent enabled: {agent_name}")
    return {"detail": f"Agent '{agent_name}' enabled"}

@router.post(
    "/agents/{agent_name}/disable",
    tags=["Agent Management"],
    summary="Disable an agent",
    response_description="Agent disabled confirmation"
)
def disable_agent(agent_name: str):
    """
    Disable a specific agent.
    """
    if agent_name not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")
    AGENTS[agent_name]["enabled"] = False
    logger.info(f"Agent disabled: {agent_name}")
    return {"detail": f"Agent '{agent_name}' disabled"}

@router.get(
    "/agents/{agent_name}",
    tags=["Agent Management"],
    summary="Get agent status",
    response_description="Agent status"
)
def get_agent_status(agent_name: str):
    """
    Get the enabled/disabled status of a specific agent.
    """
    if agent_name not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {agent_name: AGENTS[agent_name]}

# Agent management state (simple in-memory for demo)
AGENTS = {
    "seo": {"enabled": True},
    "analytics": {"enabled": True},
    "video": {"enabled": True},
    "carousel": {"enabled": True}
}


class TopicRequest(BaseModel):
    topic: str = Field(..., min_length=3, max_length=100, description="Main topic (3-100 chars)")
    posts_per_month: int = Field(12, ge=1, le=100, description="Number of posts per month (1-100)")
    include_seo: bool = False
    include_analytics: bool = False
    include_video: bool = False
    include_carousel: bool = False

class ContentItemRequest(BaseModel):
    topic: str = Field(..., min_length=3, max_length=100, description="Topic (3-100 chars)")
    category: str = Field(..., min_length=2, max_length=50, description="Category (2-50 chars)")
    tone: str = Field(..., min_length=2, max_length=30, description="Tone (2-30 chars)")
    content: str = Field(..., min_length=5, description="Content must be at least 5 characters")
    visuals: str = Field(..., min_length=3, description="Visuals must be at least 3 characters")
    seo: str = None
    analytics: str = None
    video: str = None
    carousel: str = None
    formatted_content: str = None
    research_points: str = None
    strategy: str = None
    topics: str = None
    visual_prompts: str = None
    writer_output: str = None

# Create DB tables if not exist
Base.metadata.create_all(bind=engine)

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
    - **include_seo**: Whether to run SEO agent
    - **include_analytics**: Whether to run analytics agent
    - **include_video**: Whether to run video agent
    - **include_carousel**: Whether to run carousel agent
    Returns a list of content items, each with topic, category, tone, content, visuals, and optional agent outputs.
    """
    content = generate_monthly_content(
        request.topic,
        request.posts_per_month,
        include_seo=request.include_seo,
        include_analytics=request.include_analytics,
        include_video=request.include_video,
        include_carousel=request.include_carousel
    )
    return {"monthly_content": content}

# CRUD Endpoints
@router.post(
    "/content",
    tags=["Content CRUD"],
    summary="Create a content item",
    response_description="ID and topic of created content item",
    responses={
        200: {
            "description": "Content item created",
            "content": {
                "application/json": {
                    "example": {"id": 1, "topic": "Test Topic"}
                }
            }
        }
    }
)
def create_content_item(item: ContentItemRequest, db: Session = Depends(get_db)):
    """
    Create a new content item.
    Request example:
    {
      "topic": "Test Topic",
      "category": "Test Category",
      "tone": "Test Tone",
      "content": "Test Content",
      "visuals": "Test Visuals"
    }
    """
    # Backend validation
    if not (3 <= len(item.topic) <= 100):
        raise HTTPException(status_code=400, detail="Topic must be 3-100 characters.")
    if not (2 <= len(item.category) <= 50):
        raise HTTPException(status_code=400, detail="Category must be 2-50 characters.")
    if not (2 <= len(item.tone) <= 30):
        raise HTTPException(status_code=400, detail="Tone must be 2-30 characters.")
    if not (len(item.content) >= 5):
        raise HTTPException(status_code=400, detail="Content must be at least 5 characters.")
    if not (len(item.visuals) >= 3):
        raise HTTPException(status_code=400, detail="Visuals must be at least 3 characters.")
    try:
        db_item = ContentItem(
            topic=item.topic,
            category=item.category,
            tone=item.tone,
            content=item.content,
            visuals=item.visuals,
            seo=item.seo,
            analytics=item.analytics,
            video=item.video,
            carousel=item.carousel,
            formatted_content=item.formatted_content,
            research_points=item.research_points,
            strategy=item.strategy,
            topics=item.topics,
            visual_prompts=item.visual_prompts,
            writer_output=item.writer_output
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        logger.info(f"Created content item: {db_item.id} ({db_item.topic})")
        return {"id": db_item.id, "topic": db_item.topic}
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to create content item: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create content item: {str(e)}")

@router.get(
    "/content/{item_id}",
    tags=["Content CRUD"],
    summary="Get a content item",
    response_description="Full content item",
    responses={
        200: {
            "description": "Content item found",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "topic": "Test Topic",
                        "category": "Test Category",
                        "tone": "Test Tone",
                        "content": "Test Content",
                        "visuals": "Test Visuals"
                    }
                }
            }
        },
        404: {"description": "Content item not found"}
    }
)
def get_content_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a content item by ID.
    Response example:
    {
      "id": 1,
      "topic": "Test Topic",
      "category": "Test Category",
      "tone": "Test Tone",
      "content": "Test Content",
      "visuals": "Test Visuals"
    }
    """
    item = db.query(ContentItem).filter(ContentItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Content item not found")
    return {
        "id": item.id,
        "topic": item.topic,
        "category": item.category,
        "tone": item.tone,
        "content": item.content,
        "visuals": item.visuals,
        "seo": item.seo,
        "analytics": item.analytics,
        "video": item.video,
        "carousel": item.carousel,
        "formatted_content": item.formatted_content,
        "research_points": item.research_points,
        "strategy": item.strategy,
        "topics": item.topics,
        "visual_prompts": item.visual_prompts,
        "writer_output": item.writer_output
    }

@router.put(
    "/content/{item_id}",
    tags=["Content CRUD"],
    summary="Update a content item",
    response_description="ID and topic of updated content item",
    responses={
        200: {
            "description": "Content item updated",
            "content": {
                "application/json": {
                    "example": {"id": 1, "topic": "Updated Topic"}
                }
            }
        },
        404: {"description": "Content item not found"}
    }
)
def update_content_item(item_id: int, item: ContentItemRequest, db: Session = Depends(get_db)):
    """
    Update a content item by ID.
    Request example:
    {
      "topic": "Updated Topic",
      "category": "Updated Category",
      "tone": "Updated Tone",
      "content": "Updated Content",
      "visuals": "Updated Visuals"
    }
    """
    db_item = db.query(ContentItem).filter(ContentItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Content item not found")
    # Backend validation
    if not (3 <= len(item.topic) <= 100):
        raise HTTPException(status_code=400, detail="Topic must be 3-100 characters.")
    if not (2 <= len(item.category) <= 50):
        raise HTTPException(status_code=400, detail="Category must be 2-50 characters.")
    if not (2 <= len(item.tone) <= 30):
        raise HTTPException(status_code=400, detail="Tone must be 2-30 characters.")
    if not (len(item.content) >= 5):
        raise HTTPException(status_code=400, detail="Content must be at least 5 characters.")
    if not (len(item.visuals) >= 3):
        raise HTTPException(status_code=400, detail="Visuals must be at least 3 characters.")
    try:
        db_item.topic = item.topic
        db_item.category = item.category
        db_item.tone = item.tone
        db_item.content = item.content
        db_item.visuals = item.visuals
        db_item.seo = item.seo
        db_item.analytics = item.analytics
        db_item.video = item.video
        db_item.carousel = item.carousel
        db_item.formatted_content = item.formatted_content
        db_item.research_points = item.research_points
        db_item.strategy = item.strategy
        db_item.topics = item.topics
        db_item.visual_prompts = item.visual_prompts
        db_item.writer_output = item.writer_output
        db.commit()
        db.refresh(db_item)
        logger.info(f"Updated content item: {db_item.id} ({db_item.topic})")
        return {"id": db_item.id, "topic": db_item.topic}
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to update content item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to update content item: {str(e)}")

@router.delete(
    "/content/{item_id}",
    tags=["Content CRUD"],
    summary="Delete a content item",
    response_description="Confirmation of deletion",
    responses={
        200: {
            "description": "Content item deleted",
            "content": {
                "application/json": {
                    "example": {"detail": "Content item deleted"}
                }
            }
        },
        404: {"description": "Content item not found"}
    }
)
def delete_content_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete a content item by ID.
    Response example:
    {
      "detail": "Content item deleted"
    }
    """
    db_item = db.query(ContentItem).filter(ContentItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Content item not found")
    db.delete(db_item)
    db.commit()
    logger.info(f"Deleted content item: {item_id}")
    return {"detail": "Content item deleted"}
