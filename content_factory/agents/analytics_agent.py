
from typing import List, Dict

def generate_analytics(topic: str, content: str, key_points: List[str], tone: str) -> Dict[str, str]:
    """
    Generate analytics metrics for a content item.
    Args:
        topic (str): The topic.
        content (str): The content to analyze.
        key_points (List[str]): Key points.
        tone (str): Content tone.
    Returns:
        Dict[str, str]: Performance metrics (views, engagement, shares).
    """
    views = 100 + len(content) * 2 + len(key_points) * 5
    engagement = round(len(content) / 10 + len(key_points), 2)
    shares = int(views * 0.1)
    return {
        "views": str(views),
        "engagement": str(engagement),
        "shares": str(shares),
        "tone": tone
    }
