import pytest
from content_factory.agents.analytics_agent import generate_analytics

def test_generate_analytics_basic():
    topic = "Dental Implants"
    content = "Dental implants are a permanent solution."
    key_points = ["long-lasting", "natural look", "easy care"]
    tone = "informative"
    analytics = generate_analytics(topic, content, key_points, tone)
    assert "views" in analytics
    assert "engagement" in analytics
    assert "shares" in analytics
    assert analytics["tone"] == tone

def test_generate_analytics_edge():
    analytics = generate_analytics("", "", [], "")
    assert isinstance(analytics["views"], str)
    assert isinstance(analytics["engagement"], str)
    assert isinstance(analytics["shares"], str)
