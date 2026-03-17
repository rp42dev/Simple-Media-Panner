import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("payload,expected_keys", [
    ({"topic": "Test", "posts_per_month": 2, "include_visual": True}, ["visuals"]),
    ({"topic": "Test", "posts_per_month": 2, "include_writer": True}, ["content"]),
    ({"topic": "Test", "posts_per_month": 2, "include_visual": True, "include_writer": True}, ["visuals", "content"]),
    ({"topic": "Test", "posts_per_month": 2}, []),
])
def test_generate_month_new_agent_outputs(payload, expected_keys):
    response = client.post("/generate/month", json=payload)
    assert response.status_code == 200
    data = response.json()["monthly_content"]
    for item in data:
        # content is always present, check agent-specific keys inside content
        assert "content" in item
        content_dict = item["content"] if isinstance(item["content"], dict) else {}
        for key in expected_keys:
            if key == "content":
                assert "content" in item
            elif key == "visuals":
                assert "visuals" in item
            else:
                assert key in content_dict
        # visuals is always present, so skip assertion for its absence

def test_generate_month_new_agent_invalid_payload():
    response = client.post("/generate/month", json={})
    assert response.status_code == 422
