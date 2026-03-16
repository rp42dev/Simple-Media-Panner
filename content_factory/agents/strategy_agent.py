from typing import List, Dict, Any

def assign_strategy(topic_list: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Assign category and tone to each topic in the list.
    Args:
        topic_list (List[str]): List of topic strings.
    Returns:
        Dict[str, Dict[str, str]]: Mapping of topic to category and tone.
    """
    mapping = {}
    for topic in topic_list:
        if "vs" in topic:
            mapping[topic] = {"category": "comparison", "tone": "informative"}
        elif "testimonials" in topic:
            mapping[topic] = {"category": "social_proof", "tone": "friendly"}
        elif "tips" in topic:
            mapping[topic] = {"category": "tip", "tone": "friendly"}
        else:
            mapping[topic] = {"category": "educational", "tone": "informative"}
    return mapping
