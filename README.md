# RAG Chatbot

This repository demonstrates a **Retrieval-Augmented Generation (RAG)** architecture integrated with **ChromaDB** and an **OpenAI GPT model** to create a chatbot that can interact with custom documents. The project leverages vector databases to provide real-time, context-aware answers by embedding documents and querying them based on user inputs.

## Code Structure Breakdown

The repository contains the following key components:

- **app.py**: The Streamlit app, allowing users to upload documents and interact with the chatbot.
- **config/**:
  - **config.py**: Configuration file for ChromaDB and OpenAI API settings.
  - **keys.py**: Fetches API keys from environment variables for secure access.
- **data/**: Storage for uploaded documents.
- **docs/chromadb_guide.ipynb**: A detailed guide on working with ChromaDB, including installation and queries.
- **main.py**: A terminal-based version of the chatbot for command-line interaction.
- **requirements.txt**: Python dependencies for the project.
- **scripts/run.sh**: A script to run the Streamlit app.
- **services/**:
  - **document_parser.py**: Handles document reading and chunking strategy.
  - **llm.py**: Manages interactions with the LLM (OpenAI GPT).
  - **vector_manager.py**: Responsible for managing the ChromaDB collection, indexing, and querying documents.
- **setup.py**: Python setup configuration for the project.
- **utils/**:
  - **log.py**: Logs application info and debug messages.
  - **models.py**: Pydantic models for documents, search results, etc.
  - **prompts.py**: Templates for LLM prompts, including context and user queries.
  - **textual.py**: Text utilities for cleaning, formatting, and summarizing content.

## Setup Instructions

Follow these steps to set up the project and run the Streamlit app:

### 1. Create a Virtual Environment
First, create a virtual environment for the project:
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment
Activate the environment:
- **For Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```
- **For Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Ensure that you have API keys for **OpenAI** and **ChromaDB**. Create a `.env` file and add your keys:
```bash
OPENAI_API_KEY=<your_openai_api_key>
```

### 5. Run the Streamlit App
To launch the chatbot, run:
```bash
streamlit run app.py
```
Or simply:
```bash
./scripts/run.sh
```

Alternatively, you can run the terminal-based version of the app:
```bash
python main.py
```

### 6. Upload a Document and Chat
Once the app is running, you can upload a PDF document and start interacting with the chatbot by asking questions based on the document’s content.

## References

- [Deployed RAG Chatbot Application](https://brouthenkamel-rag-chatbot-app-xbvwju.streamlit.app/)
- [Chroma Documentation](https://docs.trychroma.com/docs/overview/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)
- [Streamlit Website](https://streamlit.io/)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Project Report](https://kamel-brouthen.notion.site/Vector-Databases-Use-Case-Project-1787584d62c2801a912bc28057a83608)
