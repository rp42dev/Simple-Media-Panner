import pytest
from content_factory.agents.seo_agent import generate_seo

def test_generate_seo_basic():
    topic = "Dental Implants"
    content = "Dental implants are a permanent solution."
    key_points = ["long-lasting", "natural look", "easy care"]
    tone = "informative"
    seo = generate_seo(topic, content, key_points, tone)
    assert "keywords" in seo
    assert topic in seo["keywords"]
    assert "meta_description" in seo
    assert "Dental Implants" in seo["title"]
    assert "informative" in seo["meta_description"]

def test_generate_seo_edge():
    seo = generate_seo("", "", [], "")
    assert isinstance(seo["keywords"], list)
    assert seo["title"] == " | Dental Content"
    assert seo["meta_description"] == " - . Tone: ."
