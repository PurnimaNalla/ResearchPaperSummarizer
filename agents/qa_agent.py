from rag import create_vector_store
from tools import answer_question


def qa_agent(state):

    print("🤖 QA Agent Running...")

    # Create vector store only if it doesn't already exist
    if state["vector_store"] is None:
        state["vector_store"] = create_vector_store(state["text"])

    answer = answer_question(
        state["vector_store"],
        state["question"]
    )

    state["answer"] = answer

    return state