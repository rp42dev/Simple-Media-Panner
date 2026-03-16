from content_factory.crews.content_cluster_crew import generate_content_cluster

from typing import List, Dict, Any

def generate_monthly_content(raw_topic: str, posts_per_month: int = 12) -> List[Dict[str, Any]]:
    """
    Generate a monthly content plan from a topic.
    Args:
        raw_topic (str): The main topic.
        posts_per_month (int): Number of posts to generate.
    Returns:
        List[Dict[str, Any]]: List of content items for the month.
    """
    cluster = generate_content_cluster(raw_topic)
    if len(cluster) >= posts_per_month:
        monthly_plan = cluster[:posts_per_month]
    else:
        # Repeat cluster to fill slots
        times = posts_per_month // len(cluster)
        monthly_plan = (cluster * times)[:posts_per_month]
    return monthly_plan
