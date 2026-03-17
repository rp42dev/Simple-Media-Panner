from content_factory.agents.writer_agent import write_content

def test_write_content():
    content = write_content("Invisalign vs braces", ["Invisible", "Effective"], "friendly")
    assert "thinking about invisalign vs braces?" in content.lower()
    assert "invisalign vs braces: invisible, effective" in content.lower()
