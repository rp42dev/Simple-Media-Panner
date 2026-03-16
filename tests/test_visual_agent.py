from content_factory.agents.visual_agent import generate_visuals

def test_generate_visuals():
    visuals = generate_visuals("Invisalign", ["Invisible"], "friendly")
    assert "image_prompt" in visuals
    assert "reel_script" in visuals
