from pydantic import BaseModel, Field
from typing import List

class little_red_book(BaseModel):
    tittles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    content: str = Field(description="小红书的正文内容")