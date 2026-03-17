import pytest
from content_factory.pipelines.monthly_content_pipeline import generate_monthly_content

class DummyDB:
    def add(self, item):
        pass
    def commit(self):
        pass

@pytest.mark.parametrize("agents", [
    {"include_seo": True},
    {"include_analytics": True},
    {"include_video": True},
    {"include_carousel": True},
    {"include_seo": True, "include_analytics": True, "include_video": True, "include_carousel": True},
    {}
])
def test_agent_outputs(agents):
    result = generate_monthly_content("Test Topic", 2, db=DummyDB(), **agents)
    for item in result:
        for agent, enabled in agents.items():
            if enabled:
                key = agent.replace("include_", "")
                assert key in item
            else:
                key = agent.replace("include_", "")
                assert key not in item
