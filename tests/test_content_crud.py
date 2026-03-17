import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test create content item
def test_create_content_item():
    response = client.post("/content", json={
        "topic": "Test Topic",
        "category": "Test Category",
        "tone": "Test Tone",
        "content": "Test Content",
        "visuals": "Test Visuals",
        "seo": "SEO output",
        "analytics": "Analytics output",
        "video": "Video output",
        "carousel": "Carousel output",
        "formatted_content": "Formatted output",
        "research_points": "Research output",
        "strategy": "Strategy output",
        "topics": "Topics output",
        "visual_prompts": "Visual prompts output",
        "writer_output": "Writer output"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["topic"] == "Test Topic"

# Test get content item
def test_get_content_item():
    # Create first
    create_resp = client.post("/content", json={
        "topic": "Get Topic",
        "category": "Get Category",
        "tone": "Get Tone",
        "content": "Get Content",
        "visuals": "Get Visuals",
        "seo": "SEO output",
        "analytics": "Analytics output",
        "video": "Video output",
        "carousel": "Carousel output",
        "formatted_content": "Formatted output",
        "research_points": "Research output",
        "strategy": "Strategy output",
        "topics": "Topics output",
        "visual_prompts": "Visual prompts output",
        "writer_output": "Writer output"
    })
    item_id = create_resp.json()["id"]
    response = client.get(f"/content/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["topic"] == "Get Topic"
    assert data["seo"] == "SEO output"
    assert data["analytics"] == "Analytics output"
    assert data["video"] == "Video output"
    assert data["carousel"] == "Carousel output"
    assert data["formatted_content"] == "Formatted output"
    assert data["research_points"] == "Research output"
    assert data["strategy"] == "Strategy output"
    assert data["topics"] == "Topics output"
    assert data["visual_prompts"] == "Visual prompts output"
    assert data["writer_output"] == "Writer output"

# Test update content item
def test_update_content_item():
    create_resp = client.post("/content", json={
        "topic": "Update Topic",
        "category": "Update Category",
        "tone": "Update Tone",
        "content": "Update Content",
        "visuals": "Update Visuals",
        "seo": "Old SEO",
        "analytics": "Old Analytics",
        "video": "Old Video",
        "carousel": "Old Carousel",
        "formatted_content": "Old Formatted",
        "research_points": "Old Research",
        "strategy": "Old Strategy",
        "topics": "Old Topics",
        "visual_prompts": "Old Visual Prompts",
        "writer_output": "Old Writer"
    })
    item_id = create_resp.json()["id"]
    response = client.put(f"/content/{item_id}", json={
        "topic": "Updated Topic",
        "category": "Updated Category",
        "tone": "Updated Tone",
        "content": "Updated Content",
        "visuals": "Updated Visuals",
        "seo": "New SEO",
        "analytics": "New Analytics",
        "video": "New Video",
        "carousel": "New Carousel",
        "formatted_content": "New Formatted",
        "research_points": "New Research",
        "strategy": "New Strategy",
        "topics": "New Topics",
        "visual_prompts": "New Visual Prompts",
        "writer_output": "New Writer"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["topic"] == "Updated Topic"

# Test delete content item
def test_delete_content_item():
    create_resp = client.post("/content", json={
        "topic": "Delete Topic",
        "category": "Delete Category",
        "tone": "Delete Tone",
        "content": "Delete Content",
        "visuals": "Delete Visuals"
    })
    item_id = create_resp.json()["id"]
    response = client.delete(f"/content/{item_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Content item deleted"
