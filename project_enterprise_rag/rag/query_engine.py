from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from project_enterprise_rag.llm_chain.groq_client import groq_complete


def get_query_engine(persist_dir: str):
    # 🔑 FORCE local embeddings (NO OpenAI)
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    storage_context = StorageContext.from_defaults(
        persist_dir=persist_dir
    )

    index = load_index_from_storage(storage_context)

    # Retriever only (NO LLM)
    retriever = index.as_retriever(similarity_top_k=5)
    return retriever


def query_with_groq(retriever, query: str) -> str:
    nodes = retriever.retrieve(query)

    context = "\n\n".join(
        node.node.get_content() for node in nodes
    )

    return groq_complete(
        context=context,
        query=query
    )
