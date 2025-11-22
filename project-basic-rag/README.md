📄 Project 1 — Document Q&A System (Basic RAG with Local Embeddings)



<img width="1536" height="1024" alt="RAG_architecture" src="https://github.com/user-attachments/assets/2954d8d5-a90a-4b20-93af-b152053bf412" />

                                                    [⚙️ Basic RAG Architecture]


🚀 Introduction

This project implements a fully local Retrieval-Augmented Generation (RAG) document question-answering system, built using:

LlamaIndex for indexing & retrieval

HuggingFace BGE embeddings (offline, no API required)

Gradio for an easy interactive UI

Docker for containerized deployment

It demonstrates how to build a practical, production-ready, offline Q&A system — ideal for beginners, freshers, and engineers building hands-on projects for their portfolio.

🏷️ Tech Badges
<p> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/LlamaIndex-RAG-orange?logo=semanticweb" /> <img src="https://img.shields.io/badge/HuggingFace-Embeddings-yellow?logo=huggingface" /> <img src="https://img.shields.io/badge/Gradio-WebUI-green?logo=googlechrome" /> <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" /> </p>

## 📑 Table of Contents
- [Introduction](#introduction)
- [Architecture Diagram (Project 1)](#architecture-diagram-project-1)
- [Features](#features)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Purpose of This Project](#purpose-of-this-project)

🚀 Features

🔹 1. Local Embedding-Based Search
Uses BAAI/bge-small-en-v1.5 for fully offline vector generation.

🔹 2. Document Indexing
Reads files → embeds text → stores in VectorStoreIndex.

🔹 3. Interactive Gradio UI
Upload → Index → Ask Questions → Get Answers.

🔹 4. No LLM Required
Pure embedding retrieval:
✔️ Fast ✔️ Free ✔️ Private ✔️ Offline

🔹 5. Docker Support
Build & run anywhere with one command.

project-basic-rag/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
│── docs/
│── screenshots/
│   ├── 01-folder-structure.png
│   ├── 02-index-document.png
│   ├── 03-indexed-status.png
│   ├── 04-query-and-answer.png
│   ├── RAG_architecture.png   <-- used in README


| Step                  | Image                                 |
| --------------------- | ------------------------------------- |
| 📁 Project Structure  | `screenshots/01-folder-structure.png` |
| 📤 Upload & Index     | `screenshots/02-index-document.png`   |
| 📌 Index Confirmation | `screenshots/03-indexed-status.png`   |
| ❓ Query & Response    | `screenshots/04-query-and-answer.png` |


2️⃣ Start the App
python app.py


Access UI at: http://localhost:7860

3️⃣ Run with Docker
docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

🧠 How It Works (High-Level Architecture)

Upload Document → LlamaIndex reads text

Convert text into embeddings (BGE-small)

Store vectors in an index

Convert user question → embedding

Perform similarity search

Return best-matching answer (pure retrieval)

🎯 Purpose of This Project

This project is designed to help you:

Understand core RAG workflows

Learn vector search, embeddings, and indexing

Build offline, local GenAI tools

Prepare for advanced RAG architectures

Strengthen your resume with practical AI/ML projects

Perfect for freshers & early-career engineers.

🧩 Next Steps (Upcoming Projects)
Project	Description
Project 2	Multi-document RAG with metadata filtering
Project 3	Hybrid RAG + LLM (retrieval + generation)
Project 4	Enterprise vector DB (Pinecone / Chroma)
Project 5	Rerankers, chunking strategies, evaluation
