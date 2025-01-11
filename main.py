from document_parser import DocumentParser
from vector_manager import VectorManager
from llm import LLM

document_parser = DocumentParser()
document_path = "./data/manuscript.pdf"
document = document_parser.read_document(document_path=document_path)
chunked_document = document_parser.create_chunks(document=document)

vector_manager = VectorManager()
vector_manager.create_collection()
vector_manager.index_chunks(chunked_document=chunked_document)

llm = LLM()

while True:
    query = input("Enter a query: ")
    search_result = vector_manager.query(query_text=query)
    response = llm.generate(prompt=query, search_result=search_result)
    
    print("[HUMAN]:", query)
    print("[AI]:", response)
    
    if query == "exit":
        break
    
vector_manager.delete_collection()