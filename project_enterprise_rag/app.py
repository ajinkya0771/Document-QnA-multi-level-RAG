import gradio as gr
from rag.query_engine import get_rag_answer


def chat_fn(message, history):
    try:
        answer, top_chunks = get_rag_answer(message)

        context_display = "\n\n".join(
            [f"📘 Chunk {i+1}:\n{chunk}" for i, chunk in enumerate(top_chunks)]
        )

        final_response = (
            f"### ✅ Answer:\n{answer}\n\n"
            f"### 📚 Retrieved Context:\n{context_display}"
        )

        return final_response

    except Exception as e:
        return f"❌ Error: {str(e)}"


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Enterprise RAG Chatbot\nAsk anything from your documents!")

    chatbot = gr.ChatInterface(
        chat_fn,
        textbox=gr.Textbox(placeholder="Ask a question...", scale=7),
        title="Enterprise RAG Search",
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
