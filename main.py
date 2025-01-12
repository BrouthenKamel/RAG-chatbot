from services.document_parser import DocumentParser
from services.vector_manager import VectorManager
from services.llm import LLM

document_parser = DocumentParser()
file_name = "sample.pdf"
# file_name = "df8de2f1-d26d-46b6-944f-450b71b4cd97.pdf"
document_path = f"./data/{file_name}"
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