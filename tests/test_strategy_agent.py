from content_factory.agents.strategy_agent import assign_strategy

def test_assign_strategy():
    topics = ["Invisalign vs braces", "Patient testimonials", "Invisalign cleaning tips"]
    mapping = assign_strategy(topics)
    assert mapping["Invisalign vs braces"]["category"] == "comparison"
    assert mapping["Patient testimonials"]["tone"] == "friendly"
    assert mapping["Invisalign cleaning tips"]["category"] == "tip"
