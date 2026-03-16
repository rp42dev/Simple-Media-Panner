from content_factory.agents.research_agent import research_topic

def test_research_topic():
    points = research_topic("Invisalign vs braces", "comparison")
    assert isinstance(points, list)
    assert "Invisalign nearly invisible" in points or len(points) == 0
