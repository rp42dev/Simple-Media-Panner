from content_factory.agents.writer_agent import write_content

def test_write_content():
    content = write_content("Invisalign vs braces", ["Invisible", "Effective"], "friendly")
    assert "Thinking about invisalign vs braces?" in content.lower()
