# 📄 Project 1 — Document Q&A System (Basic RAG with Local Embeddings)

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
- [Architecture Diagram (Project 1)](#-architecture-diagram-project-1)
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

It demonstrates a complete offline RAG workflow.

---

## 🧱 Architecture Diagram (Project 1)

![Basic RAG Architecture](./screenshots/RAG_architecture.png)

---

## Features

### 🔹 1. Local Embedding-Based Search  
Uses the **BAAI/bge-small-en-v1.5** embedding model from HuggingFace.

### 🔹 2. Document Indexing  
Documents are read via `SimpleDirectoryReader`, embedded, and stored in a `VectorStoreIndex`.

### 🔹 3. Interactive Gradio UI  
Allows users to:
- Upload a file  
- Index its content  
- Ask natural-language questions  
- View retrieved answers  

### 🔹 4. No LLM Required  
Pure retrieval-based answering, making it:
- Fast  
- Lightweight  
- Free  
- Private  

### 🔹 5. Dockerized  
Can be built and run anywhere:

```sh
docker build -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic

