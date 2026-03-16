from typing import Dict, Any

def format_content_for_platforms(content: str) -> Dict[str, Any]:
    """
    Format written content for multiple platforms.
    Args:
        content (str): The content to format.
    Returns:
        Dict[str, Any]: Platform-specific content structure.
    """
    return {
        "instagram": content,
        "facebook": content,
        "linkedin": content,
        "carousel_slides": [f"Slide 1: {content}", f"Slide 2: Key Points"]
    }
