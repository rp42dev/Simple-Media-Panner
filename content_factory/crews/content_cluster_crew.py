from content_factory.agents.topic_agent import generate_topics
from content_factory.agents.strategy_agent import assign_strategy
from content_factory.agents.research_agent import research_topic
from content_factory.agents.writer_agent import write_content
from content_factory.agents.formatter_agent import format_content_for_platforms
from content_factory.agents.visual_agent import generate_visuals

from typing import List, Dict, Any

def generate_content_cluster(raw_topic: str) -> List[Dict[str, Any]]:
    """
    Orchestrate all agents to generate a content cluster for a topic.
    Args:
        raw_topic (str): The main topic.
    Returns:
        List[Dict[str, Any]]: List of content items for the topic cluster.
    """
    topics = generate_topics(raw_topic)
    strategy_map = assign_strategy(topics)
    cluster_output = []
    for topic in topics:
        category = strategy_map[topic]["category"]
        tone = strategy_map[topic]["tone"]
        key_points = research_topic(topic, category)
        written = write_content(topic, key_points, tone)
        formatted = format_content_for_platforms(written)
        visuals = generate_visuals(topic, key_points, tone)
        cluster_output.append({
            "topic": topic,
            "category": category,
            "tone": tone,
            "content": formatted,
            "visuals": visuals
        })
    return cluster_output
