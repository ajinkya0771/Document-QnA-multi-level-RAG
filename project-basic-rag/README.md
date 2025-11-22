
📄 Project 1 — Document Q&A System (Basic RAG with Local Embeddings)

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/LlamaIndex-RAG-orange?logo=semanticweb" />
  <img src="https://img.shields.io/badge/HuggingFace-Embeddings-yellow?logo=huggingface" />
  <img src="https://img.shields.io/badge/Gradio-WebUI-green?logo=googlechrome" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" />
</p>

---

## 📑 Table of Contents

- [Introduction](#introduction)
- [Architecture Diagram (Project 1)](#architecture-diagram-project-1)
- [Features](#features)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Purpose of This Project](#purpose-of-this-project)


---

## Introduction

This project is a **fully local** Document Question-Answering system using:

- **LlamaIndex**
- **HuggingFace local embedding models**
- **Gradio UI**
- **No external APIs**

It demonstrates how a Retrieval-Augmented Generation (RAG) pipeline works **without any LLM**, relying purely on embedding-based retrieval.

---

## 🧱 Architecture Diagram (Project 1)

> **This is the exact diagram you dragged & dropped — kept as you want.**

![RAG Architecture](screenshots/RAG_architecture.png)

---

## 🚀 Features

### 🔹 1. Local Embedding-Based Search  
Uses **BAAI/bge-small-en-v1.5** embedding model running fully offline.

### 🔹 2. Document Indexing  
Documents are read via `SimpleDirectoryReader`, converted into vector embeddings, and stored in a **VectorStoreIndex**.

### 🔹 3. Interactive Web UI (Gradio)  
Upload → Index → Ask questions → View answers.

### 🔹 4. Pure Retrieval (No LLM Required)  
✔ Fast  
✔ Lightweight  
✔ Free  
✔ Privacy-safe  

### 🔹 5. Dockerized End-to-End  
Build & run with:

docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

yaml
Copy code

---

## 📁 Project Structure

project-basic-rag/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
│── docs/
│── screenshots/
│ ├── 01-folder-structure.png
│ ├── 02-index-document.png
│ ├── 03-indexed-status.png
│ ├── 04-query-and-answer.png
│ ├── RAG_architecture.png

yaml
Copy code

---

## 🖼️ Screenshots

| Step | Image |
|------|-------|
| 📁 Project Structure | `screenshots/01-folder-structure.png` |
| 📤 Document Upload | `screenshots/02-index-document.png` |
| 📌 Index Confirmation | `screenshots/03-indexed-status.png` |
| ❓ Query + Answer | `screenshots/04-query-and-answer.png` |

---

## ▶️ How to Run

### 1️⃣ Install Dependencies  
pip install -r requirements.txt

bash
Copy code

### 2️⃣ Start the App  
python app.py

bash
Copy code

Open: **http://localhost:7860**

### 3️⃣ Run on Docker  
docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

yaml
Copy code

---

## 🧠 How It Works (High-Level Architecture)

1. **Upload Document** → Read with LlamaIndex  
2. **Embed Document** → Convert into vector embeddings  
3. **Store in Vector Index** → Efficient similarity search  
4. **User Query** → Convert question → embedding  
5. **Retrieve Relevant Chunks**  
6. **Return Answer** → Pure retrieval, no generation  

---

## 🎯 Purpose of This Project

This project helps you:

- Build foundations of **RAG systems**
- Understand **vector embeddings**
- Learn **local, offline retrieval**
- Prepare for advanced RAG systems in future projects
- Strengthen your portfolio for **AI/ML Engineer**, **Data Engineer**, **GenAI Engineer** roles

Perfect for a **fresher** showcasing real hands-on GenAI projects.

---

## 🧩 Next Steps (Upcoming Projects)

👉 **Project 2:** Multi-document RAG with metadata filtering  
👉 **Project 3:** Hybrid RAG + LLM  
👉 **Project 4:** Enterprise Vector DB (Pinecone / ChromaDB)  
👉 **Project 5:** RAG evaluation, chunking strategies, rerankers  

---

## 📜 License

This project is open-source and free to use for learning and portfolio building.
