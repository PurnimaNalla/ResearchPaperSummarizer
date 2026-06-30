from rag import create_vector_store


def pdf_agent(state):

    print("📄 PDF Agent Running")

    if state["vector_store"] is None:
        state["vector_store"] = create_vector_store(state["text"])

    return state