from typing import List, Dict

def generate_visuals(topic: str, key_points: List[str], tone: str) -> Dict[str, str]:
    """
    Generate visual prompts and scripts for a topic.
    Args:
        topic (str): The topic.
        key_points (List[str]): Key points to visualize.
        tone (str): The tone for visuals.
    Returns:
        Dict[str, str]: Visual prompts and scripts.
    """
    return {
        "image_prompt": f"{topic}, happy patient, dental clinic, Ireland, realistic style",
        "reel_script": f"Quick tips on {topic.lower()} for busy patients in Ireland"
    }
