from content_factory.agents.formatter_agent import format_content_for_platforms

def test_format_content_for_platforms():
    content = "Sample content"
    formatted = format_content_for_platforms(content)
    assert "instagram" in formatted
    assert "carousel_slides" in formatted
