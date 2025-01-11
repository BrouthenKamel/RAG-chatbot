from enum import Enum

CHUNK_SIZE = 100 # Number of words in a chunk
OVERLAP = 20 # Number of words to overlap between chunks

EMBEDDING_MODEL = "text-embedding-3-small" # see https://platform.openai.com/docs/models for more models
LLM_MODEL = "gpt-4o-mini" # see https://platform.openai.com/docs/models for more models
LLM_TEMPERATURE = 0.5

COLLECTION_NAME = "document_chunks" # Name of the ChromaDB collection

SPACE = "cosine" # see https://docs.trychroma.com/docs/collections/configure for more distance metrics
CONSTRUCTION_EF = 100
SEARCH_EF = 100
MAX_NEIGHBORS = 100

# DISTANCE_THRESHOLD = 0.5