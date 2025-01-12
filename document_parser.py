import fitz
from models import Page, Document, ChunkedPage, ChunkedDocument
from utils import clean_text
from config import CHUNK_SIZE, OVERLAP

from log import get_logger
logger = get_logger("Document Parser")

class DocumentParser():
    
    def __init__(self):
        self.chunk_size = CHUNK_SIZE
        self.overlap = OVERLAP
        
        logger.info("Initialized Document Parser.")
    
    def read_document(self, document_path: str) -> Document:
        
        document_raw = fitz.open(document_path)
        document = Document(pages=[])
        n_pages = document_raw.page_count
        
        for page_num in range(len(document_raw)):
            page_raw = document_raw[page_num]
            page_content = page_raw.get_text()
            page_content = clean_text(page_content)
            if page_content != "":
                document.pages.append(Page(number=page_num+1, content=page_content))

        document_raw.close()
        
        logger.info(f"Document read from '{document_path}' with {n_pages} Pages.")
        return document
    
    def create_chunks(self, document: Document) -> ChunkedDocument:
        chunked_document = ChunkedDocument(pages=[])
        n_chunks = 0
        
        for page in document.pages:
            words = page.content.split()
            chunks = []
            start = 0

            while start < len(words):
                end = start + self.chunk_size
                chunk = " ".join(words[start:end])
                chunks.append(chunk.strip())
                n_chunks += 1
                start = end - self.overlap if end - self.overlap > start else end

            chunked_page = ChunkedPage(number=page.number, chunks=chunks)
            chunked_document.pages.append(chunked_page)
        
        logger.info(f"Document chunked into {n_chunks} Chunks.")
        return chunked_document

    def display_docuement(self, document: Document):
        repeat = 20
        print("DOCUMENT")
        print("="*repeat)
        for page in document.pages:
            print(f"PAGE [{page.number}]")
            print("-"*repeat)
            print(page.content)
            print("="*repeat)

    def display_chunked_document(self, chunked_document: ChunkedDocument):
        repeat = 20
        print("CHUNKED DOCUMENT")
        print("="*repeat)
        for page in chunked_document.pages:
            print(f"PAGE [{page.number}]")
            print("-"*repeat)
            for chunk in page.chunks:
                print(chunk)
                print("-"*repeat)
            print("="*repeat)
    
if __name__ == "__main__":
    document_parser = DocumentParser()
    document_path = "./data/manuscript.pdf"
    document = document_parser.read_document(document_path=document_path)
    # document_parser.display_docuement(document=document)
    chunked_document = document_parser.create_chunks(document=document)
    # document_parser.display_chunked_document(chunked_document=chunked_document)

class DocumentParser():
    
    def __init__(self):
        self.chunk_size = CHUNK_SIZE
        self.overlap = OVERLAP
        
        logger.info("Initialized Document Parser.")
    
    def read_document(self, document_path: str) -> Document:
        
        document_raw = fitz.open(document_path)
        document = Document(pages=[])
        n_pages = document_raw.page_count
        
        for page_num in range(len(document_raw)):
            page_raw = document_raw[page_num]
            page_content = page_raw.get_text()
            page_content = clean_text(page_content)
            if page_content != "":
                document.pages.append(Page(number=page_num+1, content=page_content))

        document_raw.close()
        
        logger.info(f"Document read from '{document_path}' with {n_pages} Pages.")
        return document
    
    def create_chunks(self, document: Document) -> ChunkedDocument:
        chunked_document = ChunkedDocument(pages=[])
        n_chunks = 0
        
        for page in document.pages:
            words = page.content.split()
            chunks = []
            start = 0

            while start < len(words):
                end = start + self.chunk_size
                chunk = " ".join(words[start:end])
                chunks.append(chunk.strip())
                n_chunks += 1
                start = end - self.overlap if end - self.overlap > start else end

            chunked_page = ChunkedPage(number=page.number, chunks=chunks)
            chunked_document.pages.append(chunked_page)
        
        logger.info(f"Document chunked into {n_chunks} Chunks.")
        return chunked_document
    