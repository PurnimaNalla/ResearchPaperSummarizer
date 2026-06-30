from typing import TypedDict, List, Any


class ResearchState(TypedDict):
    text: str
    question: str

    summary: str
    answer: str
    keywords: str

    vector_store: Any
    retrieved_chunks: List[str]

    evaluation: str

    action: str
    