from typing import List

def research_topic(topic: str, category: str) -> List[str]:
    """
    Research key points for a given topic and category.
    Args:
        topic (str): The topic to research.
        category (str): The category of the topic.
    Returns:
        List[str]: List of key points.
    """
    # In practice: query LLM or local DB
    sample_points = {
        "Invisalign vs braces": ["Invisalign nearly invisible", "Braces more visible", "Both effective"],
        "Invisalign cleaning tips": ["Brush before reinserting", "Use cleaning crystals", "Avoid hot water"]
    }
    return sample_points.get(topic, [])
