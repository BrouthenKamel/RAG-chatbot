import streamlit as st
from uuid import uuid4
from document_parser import DocumentParser
from vector_manager import VectorManager
from llm import LLM

document_parser = DocumentParser()
vector_manager = VectorManager()
llm = LLM()

st.title("RAG Chatbot")
st.sidebar.header("Upload Document")

if "uploaded" not in st.session_state:
    st.session_state["uploaded"] = False

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

uploaded_file = st.sidebar.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None and not st.session_state["uploaded"]:
    document_path = f"./data/{str(uuid4())}.pdf"
    with open(document_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.sidebar.success(f"Uploaded {uploaded_file.name}")
    
    with st.spinner("Reading and processing the document..."):
        document = document_parser.read_document(document_path=document_path)
        chunked_document = document_parser.create_chunks(document=document)
        vector_manager.create_collection()
        vector_manager.index_chunks(chunked_document=chunked_document)
        st.session_state["uploaded"] = True
        st.sidebar.success("Document processed and indexed!")

st.header("Ask a Question")
query = st.text_input("Enter your query:")

if query:
    if st.session_state["uploaded"]:
        with st.spinner("Generating response..."):
            search_result = vector_manager.query(query_text=query)
            response = llm.generate(prompt=query, search_result=search_result)
            st.session_state["chat_history"].append({"query": query, "response": response})
            st.subheader("Response")
            st.write(response)
    else:
        st.warning("Please upload a document first!")

# Chat History Section
if st.session_state["chat_history"]:
    st.header("Chat History")
    for entry in st.session_state["chat_history"]:
        # Using markdown for better formatting
        st.markdown(f"**You:** {entry['query']}")
        st.markdown(f"**AI:** {entry['response']}")
        st.markdown("---")  # Adding a separator between messages for clarity
