# Project 2 — Enterprise Document Q&A System (Advanced RAG)

<p>
<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
<img src="https://img.shields.io/badge/LlamaIndex-RAG-orange" />
<img src="https://img.shields.io/badge/LlamaParse-Parsing-purple" />
<img src="https://img.shields.io/badge/MixedBread-Embeddings-yellow" />
<img src="https://img.shields.io/badge/Groq-LLM-black" />
<img src="https://img.shields.io/badge/Gradio-WebUI-green" />
<img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" />
</p>

---

## Table of Contents

- [Overview](#overview)
- [Architecture Diagram (Project 2)](#architecture-diagram-project-2)
- [Features](#features)
- [Project Structure](#project-structure)
- [Execution Flow (Screenshots)](#execution-flow-screenshots)
- [How to Run](#how-to-run)
- [Purpose of This Project](#purpose-of-this-project)
- [Whats Next](#whats-next)

---

## Overview

This project implements an **enterprise-grade Retrieval-Augmented Generation (RAG)** system for document question answering.

Unlike basic RAG pipelines, this system demonstrates:

- High-quality document parsing
- Structured chunking and normalization
- Persistent vector storage
- Production-style retrieval and query engine
- End-to-end execution proof (UI + logs)

---

## Architecture Diagram (Project 2)

![Enterprise RAG Architecture](./screenshots/enterprise_rag_architecture.png)

---

## Features

### 1. Advanced Document Parsing
Uses **LlamaParse** to extract structured content (text, tables, metadata) from PDFs.

### 2. Structured Chunking and Normalization
Parsed documents are normalized into **JSON-based chunks** to ensure reliable indexing and retrieval.

### 3. High-Quality Embeddings
Uses **MixedBread embeddings** for semantic search, with fallback support for HuggingFace embeddings.

### 4. Persistent Vector Store
Embeddings are stored on disk, enabling:
- Reuse across sessions
- Faster query performance
- Enterprise-style persistence

### 5. Context-Aware Retrieval
Retrieval is handled using **LlamaIndex query engines** with structured context injection.

### 6. LLM-Powered Answer Generation
Final answers are generated using **Groq LLM**, grounded strictly on retrieved context.

### 7. Interactive UI
Gradio-based UI supports:
- Document upload
- Index creation
- Query execution
- Answer visualization

---

## Project Structure
```
project_enterprise_rag/
│── embeddings/
│── ingestion/
│── llm_chain/
│── rag/
│── storage/
│── frontend/
│── screenshots/
│── app.py
│── api.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## Execution Flow (Screenshots)

All screenshots are available in the `screenshots/` folder  
**in strict pipeline order**, including:

- API key configuration
- Document parsing (before and after)
- Structured JSON output
- Vector store creation
- Embedding and indexing
- Query execution
- UI interaction
- Groq response logs

These screenshots serve as **execution evidence**, not just visuals.

---

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file
GROQ_API_KEY=your_key_here
MIXEDBREAD_API_KEY=your_key_here
LLAMACLOUD_API_KEY=your_key_here

# 3. Run the application
python app.py
```
Open in browser:

http://localhost:7860

## Purpose of This Project

This project is designed to demonstrate real-world enterprise RAG skills, including:

Production-style data ingestion

Parsing unstructured documents into structured formats

Embedding strategy selection

Vector persistence and retrieval

LLM orchestration

Debugging using logs and execution evidence

This goes beyond tutorials and reflects how RAG systems are built in real AI teams.

## Whats Next

FastAPI-based backend API

Fully Dockerized deployment

Multi-document ingestion

Authentication and rate limiting

Optional cloud deployment

Author

Ajinkya Dhote
AI / ML Engineer (Fresher)
Focused on GenAI, RAG Systems, and Production ML
