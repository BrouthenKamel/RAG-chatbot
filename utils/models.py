from typing import List
from pydantic import BaseModel

class Page(BaseModel):
    number: int
    content: str
    
class ChunkedPage(BaseModel):
    number: int
    chunks: List[str]

class Document(BaseModel):
    pages: List[Page]
    
class ChunkedDocument(BaseModel):
    pages: List[ChunkedPage]

class SearchResult(BaseModel):
    distances: List[float]
    documents: List[str]

class Interaction(BaseModel):
    user: str
    chatbot: str
    
class ChatHistory(BaseModel):
    interactions: List[Interaction]
