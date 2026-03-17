
from typing import List, Dict

def generate_video(topic: str, content: str, key_points: List[str], tone: str) -> Dict[str, str]:
    """
    Generate video script and metadata for a content item.
    Args:
        topic (str): The topic.
        content (str): The content to summarize.
        key_points (List[str]): Key points for the video.
        tone (str): The tone for the script.
    Returns:
        Dict[str, str]: Video script and metadata.
    """
    script = f"Welcome to our video on {topic}!\n"
    script += f"Summary: {content[:100]}...\n"
    script += "Key points:\n"
    for point in key_points:
        script += f"- {point}\n"
    script += f"\nPresented in a {tone} tone."
    meta = f"Length: {max(1, len(script)//50)} min, Tone: {tone}, Topic: {topic}"
    return {
        "video_script": script,
        "video_meta": meta
    }
