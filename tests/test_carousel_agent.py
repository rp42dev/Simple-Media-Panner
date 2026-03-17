import pytest
from content_factory.agents.carousel_agent import generate_carousel

def test_generate_carousel_basic():
    topic = "Dental Implants"
    content = "Dental implants are a permanent solution."
    key_points = ["long-lasting", "natural look", "easy care"]
    tone = "friendly"
    carousel = generate_carousel(topic, content, key_points, tone)
    assert "slides" in carousel
    assert "meta" in carousel
    assert carousel["meta"]["total_slides"] == 4
    assert topic in carousel["meta"]["topic"]
    assert tone in carousel["meta"]["tone"]

def test_generate_carousel_edge():
    carousel = generate_carousel("", "", [], "")
    assert isinstance(carousel["slides"], list)
    assert isinstance(carousel["meta"], dict)
