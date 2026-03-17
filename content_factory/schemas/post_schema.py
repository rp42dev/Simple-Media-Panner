from pydantic import BaseModel
from typing import Dict, Any

class PostSchema(BaseModel):
    topic: str
    category: str
    tone: str
    content: Dict[str, Any]
    visuals: Dict[str, Any]
    seo: str = None
    analytics: str = None
    video: str = None
    carousel: str = None
