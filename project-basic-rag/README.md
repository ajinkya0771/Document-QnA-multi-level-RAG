📄 Project 1 — Document Q&A System (Basic RAG with Local Embeddings)

This project is a fully local Document Question-Answering system built using LlamaIndex, HuggingFace embedding models, and Gradio.
It demonstrates how to:

📥 Upload and index documents

🔍 Convert documents into vector embeddings

❓ Ask questions based on document content

💬 Retrieve accurate answers using similarity search

🚫 Run without any external API calls (No OpenAI keys required)

🐳 Package and run the entire app using Docker

This is the first project in my multi-level RAG (Retrieval-Augmented Generation) series, starting from basics and moving toward advanced RAG pipelines.

🚀 Features
🔹 1. Local Embedding-Based Search

Uses the BAAI/bge-small-en-v1.5 embedding model from HuggingFace, running completely offline.

🔹 2. Document Indexing

Uploaded documents are read using SimpleDirectoryReader, converted into vector representations, and stored in a VectorStoreIndex.

🔹 3. Interactive UI with Gradio

User-friendly interface to:

Upload a file

Index the content

Ask natural language questions

View answers

🔹 4. No LLM Required

The system performs pure embedding similarity search, making it:

✔️ Fast
✔️ Lightweight
✔️ Free
✔️ Privacy-safe

🔹 5. Dockerized

The entire app can be built and deployed using:

docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

🏗️ Tech Stack
Component	Purpose
Python 3.10+	Core implementation
LlamaIndex	Document loading & vector index
HuggingFace Embeddings	Local embedding model
Gradio	Web UI
Docker	Containerization
📁 Project Structure
project-basic-rag/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
│── docs/
│── screenshots/
│     ├── 01-folder-structure.png
│     ├── 02-index-document.png
│     ├── 03-indexed-status.png
│     ├── 04-query-and-answer.png

🖼️ Screenshots
Step	Image
📁 Project Structure	screenshots/01-folder-structure.png
📤 Document Upload & Index	screenshots/02-index-document.png
📌 Index Confirmation	screenshots/03-indexed-status.png
❓ Query & Final Answer	screenshots/04-query-and-answer.png
▶️ How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start the App
python app.py


Then open: http://localhost:7860

3️⃣ Using Docker
docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

🧠 How It Works (High-Level Architecture)

Upload Document → Read via LlamaIndex

Embed Document → Convert text into vectors using BGE-small

Store in Vector Index → Efficient similarity search

User Query → Convert question → embedding

Similarity Search → Retrieve relevant chunks

Return Answer → Pure retrieval, no LLM generation

🎯 Purpose of This Project

This project is designed to:

Build foundational understanding of RAG systems

Learn how vector embeddings work

Build a local, offline, and free Q&A pipeline

Prepare for advanced RAG architectures in Project 2 & 3

Strengthen portfolio for AI/ML Engineer, Data Engineer, and GenAI Engineer roles

It is ideal for a fresher showcasing practical hands-on experience with Retrieval-Augmented Generation.

🧩 Next Steps (Upcoming Projects)

Project 2: Multi-document RAG with metadata filtering

Project 3: Hybrid RAG + LLM (Generation + Retrieval)

Project 4: Enterprise-level Vector Database (Pinecone / ChromaDB)

Project 5: RAG with rerankers, chunking strategies, and evaluation

📜 License

This project is open-source and free to use for learning and portfolio purposes.
