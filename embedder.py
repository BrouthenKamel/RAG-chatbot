from keys import OPENAI_API_KEY
from config import EMBEDDING_MODEL
import numpy as np
from openai import OpenAI
from typing import List

def openai_embedding(texts: List[str]) -> np.ndarray:
    client = OpenAI(api_key=OPENAI_API_KEY)
    embeddings = [res.embedding for res in client.embeddings.create(input=texts, model=EMBEDDING_MODEL).data]
    return embeddings

# class Embedder():
    
#     def __init__(self) -> None:
#         self.model = EMBEDDING_MODEL
#         self.client = OpenAI(api_key=OPENAI_API_KEY)
        
#     def get_embeddings(self, texts: List[str]) -> np.ndarray:
#         embeddings = np.array(
#             [res.embedding for res in self.client.embeddings.create(input=texts, model=self.model).data]
#         )
#         return embeddings
