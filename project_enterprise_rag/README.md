📄 Project 2 — Enterprise Document Q&A System (Advanced RAG)

Tech Stack: LlamaIndex · LlamaParse · MixedBread · Groq · Python · Vector Stores · Gradio
Level: Enterprise / Production-style RAG Pipeline

🔍 Overview

This project implements an enterprise-grade Retrieval-Augmented Generation (RAG) system for document question answering.

Unlike basic RAG systems, this pipeline demonstrates:

High-quality document parsing

Structured data normalization

Persistent vector storage

Production-style query engine design

End-to-end execution proof with logs and UI

The system enables users to upload large documents (PDFs), index them into a vector store, and query them using a Groq-powered LLM with MixedBread embeddings.

🧠 Key Capabilities

📄 Advanced Document Parsing using LlamaParse

🧩 Structured Chunking & Normalization (JSON-based)

🔢 High-quality Embeddings via MixedBread (with HF fallback)

🗂 Persistent Vector Store (local disk)

🔍 Context-aware Retrieval using LlamaIndex

🤖 LLM-powered Answer Generation via Groq

🖥 Interactive UI for upload, indexing, and querying

🧾 Execution Evidence (logs, API usage, terminal proof)

🏗️ Architecture (High Level)
PDF / TXT Document
        ↓
LlamaParse (High-Quality Parsing)
        ↓
Structured Output (Text + Tables + Metadata)
        ↓
Normalized JSON Chunks
        ↓
MixedBread Embeddings
        ↓
Persistent Vector Store
        ↓
Query Engine (LlamaIndex)
        ↓
Groq LLM Response
        ↓
UI / Terminal Output

📁 Project Structure
project_enterprise_rag/
│── embeddings/        # Embedding logic & configs
│── ingestion/         # Parsing, validation, normalization
│── llm_chain/         # Groq LLM client & prompt logic
│── rag/               # Query engine & retrieval logic
│── storage/           # Persistent vector store files
│── frontend/          # UI components
│── screenshots/       # End-to-end execution proof
│── app.py             # UI entry point
│── api.py             # API entry point (future FastAPI)
│── Dockerfile         # Containerization support
│── requirements.txt
│── README.md

🧪 Execution Flow — Step-by-Step (Screenshots)

The following screenshots demonstrate the complete enterprise RAG pipeline, executed end to end.

🔹 Setup & Configuration

Folder Structure (VS Code)

MixedBread API Key Configuration

Groq API Key Configuration

LlamaCloud API Key Setup

🔹 Document Parsing (LlamaParse)

Raw Document Before Parsing

LlamaParse Playground

LlamaParse Code Snippet (Python – Basic)

LlamaParse Code Snippet (Python – Full)

Parsed Structured Output

Normalized JSON Chunks

Table Layout Validation

🔹 Vector Store Creation

Vector Store Created (Empty)

Add Files Dialog

Parsing Strategy Selection

Store After Upload (Processing → Completed)

🔹 Embeddings & Indexing

Embedding Playground Output

Vector Index Created & Persisted (Local)

Vector Store After Indexing

🔹 Query & Answering

Query Engine Code Implementation

RAG Query Test (Terminal)

Uploading Document via UI

Chat Response (Answer Generation)

Groq Logs (Response Evidence)

📂 All screenshots are available in the /screenshots folder in sequential order.

▶️ How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Set Environment Variables

Create a .env file:

GROQ_API_KEY=your_key_here
MIXEDBREAD_API_KEY=your_key_here
LLAMACLOUD_API_KEY=your_key_here

3️⃣ Run the Application
python app.py


Open:

http://localhost:7860

🎯 Purpose of This Project

This project is designed to showcase real enterprise RAG skills, including:

Production-style data ingestion

Parsing unstructured documents into structured formats

Embedding strategy selection

Vector persistence and retrieval

LLM orchestration

Debugging with logs and execution evidence

It is intentionally built to go beyond tutorials and reflect how RAG systems are implemented in real-world AI teams.

🚀 What’s Next (Planned Enhancements)

✅ FastAPI-based backend API

✅ Fully Dockerized deployment

⏭ Multi-document ingestion

⏭ Authentication & rate limiting

⏭ Cloud deployment (optional)

🧑‍💻 Author

Ajinkya Dhote
AI / ML Engineer (Fresher)
Focused on GenAI, RAG Systems, and Production ML
