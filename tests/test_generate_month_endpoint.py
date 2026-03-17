import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("payload,expected_keys", [
    ({"topic": "Test", "posts_per_month": 2, "include_seo": True}, ["seo"]),
    ({"topic": "Test", "posts_per_month": 2, "include_analytics": True}, ["analytics"]),
    ({"topic": "Test", "posts_per_month": 2, "include_video": True}, ["video"]),
    ({"topic": "Test", "posts_per_month": 2, "include_carousel": True}, ["carousel"]),
    ({"topic": "Test", "posts_per_month": 2, "include_seo": True, "include_analytics": True, "include_video": True, "include_carousel": True}, ["seo", "analytics", "video", "carousel"]),
    ({"topic": "Test", "posts_per_month": 2}, []),
])
def test_generate_month_agent_outputs(payload, expected_keys):
    response = client.post("/generate/month", json=payload)
    assert response.status_code == 200
    data = response.json()["monthly_content"]
    for item in data:
        for key in expected_keys:
            assert key in item
        for key in ["seo", "analytics", "video", "carousel"]:
            if key not in expected_keys:
                assert key not in item

def test_generate_month_invalid_payload():
    response = client.post("/generate/month", json={})
    assert response.status_code == 422
