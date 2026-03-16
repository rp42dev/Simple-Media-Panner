from content_factory.agents.topic_agent import generate_topics

def test_generate_topics():
    topics = generate_topics("Invisalign")
    assert isinstance(topics, list)
    assert len(topics) >= 1
    assert any("Invisalign" in t for t in topics)
