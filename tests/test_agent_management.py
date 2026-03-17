import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agent_management_endpoints():
    # List agents
    res = client.get("/agents")
    assert res.status_code == 200
    agents = res.json()["agents"]
    assert "seo" in agents and "analytics" in agents

    # Disable SEO agent
    res = client.post("/agents/seo/disable")
    assert res.status_code == 200
    assert res.json()["detail"] == "Agent 'seo' disabled"
    # Check status
    res = client.get("/agents/seo")
    assert res.status_code == 200
    assert not res.json()["seo"]["enabled"]

    # Enable SEO agent
    res = client.post("/agents/seo/enable")
    assert res.status_code == 200
    assert res.json()["detail"] == "Agent 'seo' enabled"
    # Check status
    res = client.get("/agents/seo")
    assert res.status_code == 200
    assert res.json()["seo"]["enabled"]

    # Invalid agent
    res = client.post("/agents/invalid/enable")
    assert res.status_code == 404
    res = client.get("/agents/invalid")
    assert res.status_code == 404
