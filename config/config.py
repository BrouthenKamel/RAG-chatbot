# Document parsing parameters
CHUNK_SIZE = 100 # Number of words in a chunk
OVERLAP = 20 # Number of words to overlap between chunks

# LLM parameters
LLM_MODEL = "gpt-4o-mini" # see https://platform.openai.com/docs/models for more models
LLM_TEMPERATURE = 0.5

# ChromaDB parameters
COLLECTION_NAME = "document_chunks"
# see https://docs.trychroma.com/docs/collections/configure for detailed explanation on configuration parameters
SPACE = "cosine" 
CONSTRUCTION_EF = 100
SEARCH_EF = 100
MAX_NEIGHBORS = 100
TOP_K = 5

# Utility parameters
SUMMARIZATION_SIZE = 8