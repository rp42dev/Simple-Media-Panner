
from typing import List, Dict

def generate_seo(topic: str, content: str, key_points: List[str], tone: str) -> Dict[str, str]:
    """
    Generate SEO metadata for a content item.
    Args:
        topic (str): The topic.
        content (str): The content to optimize.
        key_points (List[str]): Key points for SEO.
        tone (str): Content tone.
    Returns:
        Dict[str, str]: SEO metadata (keywords, meta description, title).
    """
    keywords = [topic] + key_points[:3]
    meta_description = f"{topic} - {'; '.join(key_points)}. Tone: {tone}."
    title = f"{topic} | Dental Content"
    return {
        "keywords": keywords,
        "meta_description": meta_description,
        "title": title
    }
