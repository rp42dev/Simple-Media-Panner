
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

// Main Home page component for the app UI
export default function Home() {
  // State for content generation form
  const [topic, setTopic] = useState("");
  const [postsPerMonth, setPostsPerMonth] = useState(12);
  const [content, setContent] = useState([]);
  // State for agent selection checkboxes
  const [selectedAgents, setSelectedAgents] = useState({
    seo: true,
    analytics: true,
    video: true,
    carousel: true
  });
  // Loading and error state for async actions
  const [loading, setLoading] = useState(false);
  const [globalError, setGlobalError] = useState("");
  const [globalLoading, setGlobalLoading] = useState(false);
  // State for CRUD content items
  const [contentItems, setContentItems] = useState([]);
  const [loadingContentItems, setLoadingContentItems] = useState(false);
  const [contentItemError, setContentItemError] = useState("");
  const [viewItem, setViewItem] = useState(null);
  // State for agent management
  const [agentStatus, setAgentStatus] = useState({});
  const [loadingAgents, setLoadingAgents] = useState({});
  const [agentError, setAgentError] = useState({});
  // Track which content item is open (for details view)
  const [openIndex, setOpenIndex] = useState(null);
  const contentRegionRef = useRef(null);

  // Fetch all content items from backend
  const fetchContentItems = async () => {
    setLoadingContentItems(true);
    setContentItemError("");
    try {
      const res = await axios.get("http://localhost:8000/content");
      setContentItems(res.data.items || []);
    } catch (err) {
      setContentItemError("Failed to load content items: " + (err.message || "Unknown error"));
    } finally {
      setLoadingContentItems(false);
    }
  };

  // Delete a content item by ID
  const deleteContentItem = async (id) => {
    setContentItemError("");
    setGlobalLoading(true);
    try {
      await axios.delete(`http://localhost:8000/content/${id}`);
      setContentItems(items => items.filter(item => item.id !== id));
      if (viewItem && viewItem.id === id) setViewItem(null);
    } catch (err) {
      setContentItemError("Delete failed: " + (err.message || "Unknown error"));
    } finally {
      setGlobalLoading(false);
    }
  };

  // Fetch agent status from backend on mount
  useEffect(() => {
    setGlobalLoading(true);
    axios.get("http://localhost:8000/agents")
      .then(res => {
        setAgentStatus(res.data.agents);
      })
      .catch(err => {
        setGlobalError("Failed to load agents: " + (err.message || "Unknown error"));
      })
      .finally(() => setGlobalLoading(false));
  }, []);

  // Enable/disable agent and refresh status
  const toggleAgent = async (agent, enabled) => {
    setLoadingAgents(prev => ({ ...prev, [agent]: true }));
    setAgentError(prev => ({ ...prev, [agent]: null }));
    setGlobalError("");
    const url = `http://localhost:8000/agents/${agent}/${enabled ? "enable" : "disable"}`;
    setGlobalLoading(true);
    try {
      await axios.post(url);
      // Refresh agent status after toggle
      const res = await axios.get("http://localhost:8000/agents");
      setAgentStatus(res.data.agents);
    } catch (err) {
      setAgentError(prev => ({ ...prev, [agent]: err.message || "Error" }));
      setGlobalError("Agent action failed: " + (err.message || "Unknown error"));
    } finally {
      setLoadingAgents(prev => ({ ...prev, [agent]: false }));
      setGlobalLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif", position: "relative" }}>
      {globalLoading && (
        <div style={{
          position: "fixed", top: 0, left: 0, width: "100vw", height: "100vh", background: "rgba(255,255,255,0.6)", zIndex: 1000,
          display: "flex", alignItems: "center", justifyContent: "center"
        }}>
          <div style={{ padding: 24, background: "#fff", borderRadius: 8, boxShadow: "0 2px 8px #0002" }}>
            <span style={{ fontSize: 24 }}>⏳</span> Loading...
          </div>
        </div>
      )}
      {globalError && (
        <div style={{ background: "#ffe0e0", color: "#a00", padding: 12, borderRadius: 6, marginBottom: 16, border: "1px solid #f99" }}>
          <strong>Error:</strong> {globalError}
          <button style={{ float: "right" }} onClick={() => setGlobalError("")}>Dismiss</button>
        </div>
      )}
      <h1>Simple Media Panner</h1>

      {/* CRUD Content Items Section */}
      <section style={{ marginBottom: 32 }}>
        <h2>Content Items (CRUD)</h2>
        <button onClick={fetchContentItems} disabled={loadingContentItems} style={{ marginBottom: 8 }}>
          {loadingContentItems ? "Loading..." : "Refresh List"}
        </button>
        {contentItemError && <div style={{ color: "#a00", marginBottom: 8 }}>{contentItemError}</div>}
        {contentItems.length === 0 ? (
          <div style={{ color: "#888" }}>No content items found.</div>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse", marginBottom: 12 }}>
            <thead>
              <tr style={{ background: "#f4f4f4" }}>
                <th>ID</th>
                <th>Topic</th>
                <th>Category</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {contentItems.map(item => (
                <tr key={item.id} style={{ borderBottom: "1px solid #eee" }}>
                  <td>{item.id}</td>
                  <td>{item.topic}</td>
                  <td>{item.category}</td>
                  <td>
                    <button onClick={() => setViewItem(item)} style={{ marginRight: 8 }}>View</button>
                    <button onClick={() => deleteContentItem(item.id)} style={{ color: "#a00" }}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
        {viewItem && (
          <div style={{ background: "#f9f9f9", border: "1px solid #ddd", borderRadius: 6, padding: 16, marginTop: 8 }}>
            <h4>Content Item Details</h4>
            <pre style={{ background: "#f4f4f4", padding: 8, borderRadius: 4, overflowX: "auto" }}>{JSON.stringify(viewItem, null, 2)}</pre>
            <button onClick={() => setViewItem(null)} style={{ marginTop: 8 }}>Close</button>
          </div>
        )}
      </section>
      <section style={{ marginBottom: 32 }}>
        <h2>Agent Management</h2>
        {Object.keys(agentStatus).length === 0 ? (
          <div>Loading agents...</div>
        ) : (
          <ul>
            {Object.entries(agentStatus).map(([agent, status]) => (
              <li key={agent} style={{ marginBottom: 8 }}>
                <strong>{agent}</strong>:
                <span style={{ margin: "0 8px" }}>
                  {status.enabled ? "Enabled" : "Disabled"}
                </span>
                <button
                  onClick={() => toggleAgent(agent, !status.enabled)}
                  disabled={loadingAgents[agent]}
                  style={{ marginRight: 8 }}
                >
                  {status.enabled ? "Disable" : "Enable"}
                </button>
                {agentError[agent] && (
                  <span style={{ color: "red" }}>{agentError[agent]}</span>
                )}
              </li>
            ))}
          </ul>
        )}
      </section>

      <section style={{ marginBottom: 32 }}>
        <h2>Generate Monthly Content</h2>
        <form
          onSubmit={async e => {
            e.preventDefault();
            setLoading(true);
            setContent([]);
            setGlobalError("");
            setGlobalLoading(true);
            try {
              const res = await axios.post("http://localhost:8000/generate/month", {
                topic,
                posts_per_month: postsPerMonth,
                include_seo: selectedAgents.seo,
                include_analytics: selectedAgents.analytics,
                include_video: selectedAgents.video,
                include_carousel: selectedAgents.carousel
              });
              setContent(res.data.monthly_content || []);
            } catch (err) {
              setContent([{ error: err.message || "Error generating content" }]);
              setGlobalError("Content generation failed: " + (err.message || "Unknown error"));
            } finally {
              setLoading(false);
              setGlobalLoading(false);
            }
          }}
        >
          <div style={{ marginBottom: 8 }}>
            <label htmlFor="topic-input">Topic: </label>
            <input
              id="topic-input"
              value={topic}
              onChange={e => setTopic(e.target.value)}
              required
              minLength={3}
              maxLength={100}
              style={{ width: 200 }}
              placeholder="e.g. Invisalign"
              title="Enter the main topic (3-100 characters)"
            />
            <span style={{ color: '#888', marginLeft: 8 }} title="Topic must be 3-100 characters">ⓘ</span>
          </div>
          <div style={{ marginBottom: 8 }}>
            <label htmlFor="posts-input">Posts per month: </label>
            <input
              id="posts-input"
              type="number"
              value={postsPerMonth}
              onChange={e => setPostsPerMonth(Number(e.target.value))}
              min={1}
              max={100}
              style={{ width: 60 }}
              title="Number of posts to generate (1-100)"
            />
            <span style={{ color: '#888', marginLeft: 8 }} title="Number of posts per month (1-100)">ⓘ</span>
          </div>
          <div style={{ marginBottom: 8 }}>
            <label>Include agents: </label>
            {Object.keys(selectedAgents).map(agent => (
              <label key={agent} style={{ marginRight: 12 }}>
                <input
                  type="checkbox"
                  checked={selectedAgents[agent]}
                  onChange={e => setSelectedAgents(prev => ({ ...prev, [agent]: e.target.checked }))}
                  style={{ marginRight: 4 }}
                />
                {agent.charAt(0).toUpperCase() + agent.slice(1)}
              </label>
            ))}
          </div>
          <button type="submit" disabled={loading || !topic}>
            {loading ? "Generating..." : "Generate"}
          </button>
        </form>
        <div ref={contentRegionRef} style={{ marginTop: 16 }}>
          {content.length > 0 && (
            <div>
              <h3>Generated Content</h3>
              <ul style={{ listStyle: "none", padding: 0 }}>
                {content.map((item, idx) => (
                  <li key={idx} style={{ marginBottom: 16, border: "1px solid #ddd", borderRadius: 6, background: "#fafbfc", boxShadow: "0 1px 2px #0001" }}>
                    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "8px 12px", cursor: "pointer" }} onClick={() => setOpenIndex(openIndex === idx ? null : idx)}>
                      <span style={{ fontWeight: 600, color: item.error ? "#a00" : "#333" }}>
                        {item.error ? `Error` : `Content Item #${idx + 1}`}
                      </span>
                      <span style={{ fontSize: 18 }}>{openIndex === idx ? "▼" : "▶"}</span>
                    </div>
                    {openIndex === idx && (
                      <div style={{ padding: 12, borderTop: "1px solid #eee", background: item.error ? "#ffeaea" : "#fff" }}>
                        {item.error ? (
                          <span style={{ color: "#a00" }}>{item.error}</span>
                        ) : (
                          <>
                            <button
                              style={{ float: "right", marginBottom: 8 }}
                              onClick={e => {
                                e.stopPropagation();
                                navigator.clipboard.writeText(JSON.stringify(item, null, 2));
                              }}
                            >Copy JSON</button>
                            <pre style={{ background: "#f4f4f4", padding: 8, borderRadius: 4, overflowX: "auto", margin: 0 }}>
                              {JSON.stringify(item, null, 2)}
                            </pre>
                          </>
                        )}
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}


