import React, { useState, useEffect } from "react";
import axios from "axios";

export default function ContentManager() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({
    topic: "",
    category: "",
    tone: "",
    content: "",
    visuals: "",
    seo: "",
    analytics: "",
    video: "",
    carousel: ""
  });
  const [editingId, setEditingId] = useState(null);

  // Fetch all content items (for demo, fetch first 10 by id)
  useEffect(() => {
    // In production, implement pagination or list endpoint
    const fetchItems = async () => {
      let fetched = [];
      for (let id = 1; id <= 10; id++) {
        try {
          const res = await axios.get(`http://localhost:8000/content/${id}`);
          fetched.push(res.data);
        } catch (err) {
          // Ignore not found
        }
      }
      setItems(fetched);
    };
    fetchItems();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleCreate = async () => {
    const res = await axios.post("http://localhost:8000/content", form);
    setItems([...items, { ...form, id: res.data.id }]);
    setForm({ topic: "", category: "", tone: "", content: "", visuals: "", seo: "", analytics: "", video: "", carousel: "" });
  };

  const handleUpdate = async () => {
    await axios.put(`http://localhost:8000/content/${editingId}`, form);
    setItems(items.map(item => item.id === editingId ? { ...form, id: editingId } : item));
    setEditingId(null);
    setForm({ topic: "", category: "", tone: "", content: "", visuals: "", seo: "", analytics: "", video: "", carousel: "" });
  };

  const handleEdit = (item) => {
    setEditingId(item.id);
    setForm({ ...item });
  };

  const handleDelete = async (id) => {
    await axios.delete(`http://localhost:8000/content/${id}`);
    setItems(items.filter(item => item.id !== id));
  };

  return (
    <div style={{ padding: 32 }}>
      <h1>Content Manager</h1>
      <div style={{ marginBottom: 24 }}>
        <input name="topic" placeholder="Topic" value={form.topic} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="category" placeholder="Category" value={form.category} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="tone" placeholder="Tone" value={form.tone} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="content" placeholder="Content" value={form.content} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="visuals" placeholder="Visuals" value={form.visuals} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="seo" placeholder="SEO" value={form.seo} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="analytics" placeholder="Analytics" value={form.analytics} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="video" placeholder="Video" value={form.video} onChange={handleChange} style={{ marginRight: 8 }} />
        <input name="carousel" placeholder="Carousel" value={form.carousel} onChange={handleChange} style={{ marginRight: 8 }} />
        {editingId ? (
          <button onClick={handleUpdate}>Update</button>
        ) : (
          <button onClick={handleCreate}>Create</button>
        )}
      </div>
      <div>
        {items.map(item => (
          <div key={item.id} style={{ border: "1px solid #ccc", padding: 16, marginBottom: 16 }}>
            <strong>{item.topic}</strong> <br />
            Category: {item.category} <br />
            Tone: {item.tone} <br />
            Content: {item.content} <br />
            Visuals: {item.visuals} <br />
            SEO: {item.seo} <br />
            Analytics: {item.analytics} <br />
            Video: {item.video} <br />
            Carousel: {item.carousel} <br />
            <button onClick={() => handleEdit(item)} style={{ marginRight: 8 }}>Edit</button>
            <button onClick={() => handleDelete(item.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}
