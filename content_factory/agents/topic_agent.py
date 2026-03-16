from typing import List

def generate_topics(raw_topic: str) -> List[str]:
    """
    Generate a cluster of subtopics from a raw topic string.
    Args:
        raw_topic (str): The main topic (e.g., 'Invisalign').
    Returns:
        List[str]: List of subtopic strings.
    """
    return [
        "Invisalign vs braces",
        "How Invisalign works",
        "Invisalign cleaning tips",
        "Cost of Invisalign in Ireland",
        "Patient testimonials"
    ]
