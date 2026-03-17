import pytest
from content_factory.agents.video_agent import generate_video

def test_generate_video_basic():
    topic = "Dental Implants"
    content = "Dental implants are a permanent solution."
    key_points = ["long-lasting", "natural look", "easy care"]
    tone = "friendly"
    video = generate_video(topic, content, key_points, tone)
    assert "video_script" in video
    assert "video_meta" in video
    assert topic in video["video_script"]
    assert tone in video["video_meta"]

def test_generate_video_edge():
    video = generate_video("", "", [], "")
    assert isinstance(video["video_script"], str)
    assert isinstance(video["video_meta"], str)
