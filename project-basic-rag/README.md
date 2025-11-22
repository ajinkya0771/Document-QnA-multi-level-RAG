# Project 1 — Basic RAG System (Local Embeddings)

Fully local document Q&A using LlamaIndex, HuggingFace BGE-small embeddings, and Gradio.
No OpenAI API key required.

## 🚀 Run using Docker

docker build --no-cache -t doc-qa-basic .
docker run -p 7860:7860 doc-qa-basic
