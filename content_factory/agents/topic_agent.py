from typing import List

def generate_topics(raw_topic: str) -> List[str]:
    """
    Generate a cluster of subtopics from a raw topic string.
    Args:
        raw_topic (str): The main topic (e.g., 'Invisalign', 'dental implant').
    Returns:
        List[str]: List of subtopic strings.
    """
    topic = raw_topic.lower()
    if "invisalign" in topic:
        return [
            "Invisalign vs braces",
            "How Invisalign works",
            "Invisalign cleaning tips",
            "Cost of Invisalign in Ireland",
            "Patient testimonials"
        ]
    elif "implant" in topic:
        return [
            "Dental implant vs bridge",
            "How dental implants work",
            "Dental implant aftercare tips",
            "Cost of dental implants in Ireland",
            "Patient testimonials"
        ]
    else:
        return [
            f"{raw_topic} overview",
            f"How {raw_topic} works",
            f"{raw_topic} tips",
            f"Cost of {raw_topic} in Ireland",
            f"Patient testimonials"
        ]
