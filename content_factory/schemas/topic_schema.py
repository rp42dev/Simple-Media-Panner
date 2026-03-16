from pydantic import BaseModel
from typing import List

class TopicSchema(BaseModel):
    raw_topic: str
    topics: List[str]
