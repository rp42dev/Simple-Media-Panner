from content_factory.crews.content_cluster_crew import generate_content_cluster
from typing import List, Dict, Any
from content_factory.agents.seo_agent import generate_seo
from content_factory.agents.analytics_agent import generate_analytics
 
from content_factory.agents.video_agent import generate_video
from content_factory.agents.carousel_agent import generate_carousel
from content_factory.database.models import ContentItem, get_db
from sqlalchemy.orm import Session

def generate_monthly_content(
    raw_topic: str,
    posts_per_month: int = 12,
    db: Session = None,
    include_seo: bool = False,
    include_analytics: bool = False,
    include_video: bool = False,
    include_carousel: bool = False
) -> List[Dict[str, Any]]:
    """
    Generate a monthly content plan from a topic, with optional agent outputs.
    Args:
        raw_topic (str): The main topic.
        posts_per_month (int): Number of posts to generate.
        include_seo, include_analytics, include_video, include_carousel: Whether to run extra agents.
        db (Session): Optional DB session.
    Returns:
        List[Dict[str, Any]]: List of content items for the month.
    """
    cluster = generate_content_cluster(raw_topic)
    if len(cluster) >= posts_per_month:
        monthly_plan = cluster[:posts_per_month]
    else:
        # Repeat cluster to fill slots
        times = posts_per_month // len(cluster)
        monthly_plan = (cluster * times)[:posts_per_month]

    # Add agent outputs
    for item in monthly_plan:
        if include_video:
            item["video"] = generate_video(
                item.get("topic", ""),
                str(item.get("content", "")),
                item.get("key_points", []),
                item.get("tone", "")
            )
        if include_seo:
            item["seo"] = generate_seo(
                item.get("topic", ""),
                str(item.get("content", "")),
                item.get("key_points", []),
                item.get("tone", "")
            )
        if include_analytics:
            item["analytics"] = generate_analytics(
                item.get("topic", ""),
                str(item.get("content", "")),
                item.get("key_points", []),
                item.get("tone", "")
            )
        if include_carousel:
            item["carousel"] = generate_carousel(
                item.get("topic", ""),
                str(item.get("content", "")),
                item.get("key_points", []),
                item.get("tone", "")
            )

    # Save each content item to DB if session provided
    if db:
        for item in monthly_plan:
            db_item = ContentItem(
                topic=item["topic"],
                category=item["category"],
                tone=item["tone"],
                content=str(item["content"]),
                visuals=str(item["visuals"])
            )
            db.add(db_item)
        db.commit()
    return monthly_plan
