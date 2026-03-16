from typing import List

def write_content(topic: str, key_points: List[str], tone: str) -> str:
    """
    Write content for a topic using key points and tone.
    Args:
        topic (str): The topic.
        key_points (List[str]): Key points to include.
        tone (str): The tone of the content.
    Returns:
        str: The written content.
    """
    # Use LLM call here
    content = f"{topic}: " + ", ".join(key_points)
    if tone == "friendly":
        content = f"Thinking about {topic.lower()}? {content}"
    return content
