
from typing import List, Dict

def generate_carousel(topic: str, content: str, key_points: List[str], tone: str) -> Dict[str, List[Dict[str, str]]]:
    """
    Generate carousel slides and metadata for a content item.
    Args:
        topic (str): The topic.
        content (str): The content to summarize.
        key_points (List[str]): Key points for slides.
        tone (str): The tone for slides.
    Returns:
        Dict[str, List[Dict[str, str]]]: Carousel slides and metadata.
    """
    slides = []
    slides.append({"slide": f"Slide 1: {topic} - {content[:60]}..."})
    for idx, point in enumerate(key_points, start=2):
        slides.append({"slide": f"Slide {idx}: {point} ({tone})"})
    meta = {"total_slides": len(slides), "tone": tone, "topic": topic}
    return {"slides": slides, "meta": meta}
