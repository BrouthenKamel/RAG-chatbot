from datetime import datetime

import chromadb
from config import COLLECTION_NAME, SPACE, CONSTRUCTION_EF, SEARCH_EF, MAX_NEIGHBORS

from models import ChunkedDocument, SearchResult
from utils import summarize

from log import get_logger
logger = get_logger("Vector Manager")

class VectorManager():
    
    def __init__(self):
        self.space = SPACE
        self.construction_ef = CONSTRUCTION_EF
        self.search_ef = SEARCH_EF
        self.max_neighbors = MAX_NEIGHBORS
        
        self.client = chromadb.PersistentClient()
        self.collection_name = COLLECTION_NAME
        
        logger.info("Initialized Vector Manager.")
        
    def create_collection(self):
        try:
            collection = self.client.create_collection(
                name=self.collection_name,
                metadata={
                    "created_at": datetime.now().isoformat(),
                    "hnsw:space": self.space,
                    "hnsw:construction_ef": self.construction_ef,
                    "hnsw:search_ef": self.search_ef,
                    "hnsw:M": self.max_neighbors
                }
            )
            logger.info(f"Created collection '{self.collection_name}'.")
            return collection
        except Exception as e:
            collection = self.client.get_collection(self.collection_name)
            logger.info(f"Collection '{self.collection_name}' already exists.")
            self.client.delete_collection(self.collection_name)
            logger.info(f"Deleted collection '{self.collection_name}'.")
            collection = self.client.create_collection(
                name=self.collection_name,
                metadata={
                    "created_at": datetime.now().isoformat(),
                    "hnsw:space": self.space,
                    "hnsw:construction_ef": self.construction_ef,
                    "hnsw:search_ef": self.search_ef,
                    "hnsw:M": self.max_neighbors
                }
            )
            logger.info(f"Created collection '{self.collection_name}'.")
            return collection
    
    def delete_collection(self):
        self.client.delete_collection(self.collection_name)
        logger.info(f"Deleted collection '{self.collection_name}'.")

    def index_chunks(self, chunked_document: ChunkedDocument):
        collection = self.client.get_collection(self.collection_name)     
        ids = []
        documents = []
        metadatas = []
        for page in chunked_document.pages:
            for i, chunk in enumerate(page.chunks):
                id = f"page-{page.number}-chunk-{i}"
                metadata = {"page_number": page.number, "chunk_index": i}
                ids.append(id)
                documents.append(chunk)
                metadatas.append(metadata)
                
        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        logger.info(f"Indexed {len(ids)} Chunks.")
        
    def query(self, query_text: str, n_results=5):
        collection = self.client.get_collection(self.collection_name)
        
        logger.debug(f"Query: '{summarize(query_text)}'")
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        n_search = len(results['ids']) if results != {} else 0
        logger.info(f"Queried collection '{self.collection_name}', Retrived {n_search} contexts.")
        
        if n_search == 0:
            return SearchResult(distances=[], documents=[])
        else:
            result = SearchResult(
                distances = results['distances'][0],
                documents = results['documents'][0]
            )
            for doc, dist in zip(result.documents, result.distances):
                logger.debug(f"Distance: {dist}, Document: '{summarize(doc)}'")
            return result
