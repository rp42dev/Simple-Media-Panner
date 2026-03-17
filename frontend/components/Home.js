import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

export default function Home() {
  const [topic, setTopic] = useState("");
  const [postsPerMonth, setPostsPerMonth] = useState(12);
  const [content, setContent] = useState([]);
  const [loading, setLoading] = useState(false);
  const [agentStatus, setAgentStatus] = useState({});
  const [loadingAgents, setLoadingAgents] = useState({});
  const [agentError, setAgentError] = useState({});
  const contentRegionRef = useRef(null);

  useEffect(() => {
    axios.get("http://localhost:8000/agents").then(res => {
      setAgentStatus(res.data.agents);
    });
  }, []);

  const toggleAgent = async (agent, enabled) => {
    setLoadingAgents(prev => ({ ...prev, [agent]: true }));
    setAgentError(prev => ({ ...prev, [agent]: null }));
    const url = `http://localhost:8000/agents/${agent}/${enabled ? "enable" : "disable"}`;
    try {
      await axios.post(url);
      setAgentStatus(prev => ({ ...prev, [agent]: { enabled } }));
    } catch (err) {
      setAgentError(prev => ({ ...prev, [agent]: err.response?.data?.detail || "Error" }));
    }
    setLoadingAgents(prev => ({ ...prev, [agent]: false }));
  };

  const handleGenerate = async () => {
    setLoading(true);
    const include_seo = agentStatus.seo?.enabled || false;
    const include_analytics = agentStatus.analytics?.enabled || false;
    const include_video = agentStatus.video?.enabled || false;
    const include_carousel = agentStatus.carousel?.enabled || false;
    try {
      const res = await axios.post("http://localhost:8000/generate/month", {
        topic,
        posts_per_month: postsPerMonth,
        include_seo,
        include_analytics,
        include_video,
        include_carousel,
      });
      setContent(res.data.monthly_content);
    } catch (err) {
      alert("Error generating content");
    }
    setLoading(false);
  };

  const agentDescriptions = {
    seo: "Search Engine Optimization agent",
    analytics: "Analytics agent for content insights",
    video: "Video content generation agent",
    carousel: "Carousel visual content agent",
    formatter: "Content formatter for platform adaptation",
    research: "Research agent for topic insights",
    strategy: "Strategy agent for content planning",
    topic: "Topic clustering agent",
    visual: "Visual prompt generation agent",
    writer: "Writer agent for content creation"
  };

  return (
    <div style={{ padding: 32 }}>
      <h1 id="main-heading" tabIndex={-1}>Dental Content Generator</h1>
      <form
        aria-labelledby="main-heading"
        onSubmit={e => { e.preventDefault(); handleGenerate(); }}
        style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 8 }}
      >
        <label htmlFor="topic-input" style={{ marginRight: 4 }}>Topic:</label>
        <input
          id="topic-input"
          type="text"
          placeholder="Enter topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          style={{ marginRight: 8 }}
          aria-required="true"
        />
        <label htmlFor="posts-input" style={{ marginRight: 4 }}>Posts/Month:</label>
        <input
          id="posts-input"
          type="number"
          value={postsPerMonth}
          onChange={(e) => setPostsPerMonth(Number(e.target.value))}
          min={1}
          style={{ marginRight: 8, width: 80 }}
          aria-required="true"
        />
        <button type="submit" onClick={handleGenerate} disabled={loading} aria-busy={loading} aria-live="polite">
          {loading ? "Generating…" : "Generate Content"}
        </button>
      </form>
      <fieldset style={{ margin: "16px 0", border: "1px solid #ccc", padding: 16 }}>
        <legend>Agent Selection</legend>
        {Object.keys(agentStatus).length === 0 ? (
          <div>No agents available</div>
        ) : (
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 12 }}>
            {Object.entries(agentStatus).map(([agent, status], idx) => (
              <div key={agent} style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", border: "1px solid #eee", borderRadius: 8, padding: 12 }}>
                <label style={{ fontWeight: "bold", marginBottom: 8, display: "flex", alignItems: "center", gap: 8 }}>
                  <input
                    type="checkbox"
                    id={`agent-${agent}`}
                    name={agent}
                    aria-describedby={`agent-desc-${agent}`}
                    checked={!!status.enabled}
                    onChange={() => toggleAgent(agent, !status.enabled)}
                    disabled={loadingAgents[agent]}
                    style={{ marginBottom: 0 }}
                    tabIndex={0}
                  />
                  {agent.charAt(0).toUpperCase() + agent.slice(1)}
                </label>
                <span id={`agent-desc-${agent}`} style={{ fontSize: 12, color: "#555" }}>
                  {agentDescriptions[agent] || "Agent for content generation"}
                </span>
                <span style={{ fontSize: 12, color: status.enabled ? "green" : "red" }}>
                  {status.enabled ? "Enabled" : "Disabled"}
                </span>
                {loadingAgents[agent] && <span aria-live="polite" style={{ color: "#007bff" }}>Updating…</span>}
                {agentError[agent] && <span aria-live="polite" style={{ color: "#d00" }}>{agentError[agent]}</span>}
              </div>
            ))}
          </div>
        )}
      </fieldset>
      <div
        ref={contentRegionRef}
        style={{ marginTop: 32 }}
        aria-live="polite"
        aria-atomic="true"
        tabIndex={-1}
      >
        {content.length === 0 && !loading && (
          <div role="status" aria-live="polite" style={{ color: "#888" }}>No content generated yet.</div>
        )}
        {content.map((item, idx) => (
          <section
            key={idx}
            style={{ marginBottom: 24, border: "1px solid #ccc", padding: 16 }}
            aria-labelledby={`content-topic-${idx}`}
            tabIndex={0}
          >
            <h2 id={`content-topic-${idx}`}>{item.topic}</h2>
            <p><strong>Category:</strong> {item.category}</p>
            <p><strong>Tone:</strong> {item.tone}</p>
            <pre>{JSON.stringify(item.content, null, 2)}</pre>
            <pre>{JSON.stringify(item.visuals, null, 2)}</pre>
            {item.seo && (
              <div>
                <h4>SEO Output</h4>
                <pre>{JSON.stringify(item.seo, null, 2)}</pre>
              </div>
            )}
            {item.analytics && (
              <div>
                <h4>Analytics Output</h4>
                <pre>{JSON.stringify(item.analytics, null, 2)}</pre>
              </div>
            )}
            {item.video && (
              <div>
                <h4>Video Output</h4>
                <pre>{JSON.stringify(item.video, null, 2)}</pre>
              </div>
            )}
            {item.carousel && (
              <div>
                <h4>Carousel Output</h4>
                <pre>{JSON.stringify(item.carousel, null, 2)}</pre>
              </div>
            )}
            {item.formatted_content && (
              <div>
                <h4>Formatted Content</h4>
                <pre>{JSON.stringify(item.formatted_content, null, 2)}</pre>
              </div>
            )}
            {item.research_points && (
              <div>
                <h4>Research Points</h4>
                <pre>{JSON.stringify(item.research_points, null, 2)}</pre>
              </div>
            )}
            {item.strategy && (
              <div>
                <h4>Strategy Output</h4>
                <pre>{JSON.stringify(item.strategy, null, 2)}</pre>
              </div>
            )}
            {item.topics && (
              <div>
                <h4>Topics Output</h4>
                <pre>{JSON.stringify(item.topics, null, 2)}</pre>
              </div>
            )}
            {item.visual_prompts && (
              <div>
                <h4>Visual Prompts</h4>
                <pre>{JSON.stringify(item.visual_prompts, null, 2)}</pre>
              </div>
            )}
            {item.writer_output && (
              <div>
                <h4>Writer Output</h4>
                <pre>{JSON.stringify(item.writer_output, null, 2)}</pre>
              </div>
            )}
          </section>
        ))}
      </div>
    </div>
  );
}
