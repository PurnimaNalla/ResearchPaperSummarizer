from typing import TypedDict, List, Any, Optional


class ResearchState(TypedDict):
    text: str
    question: str

    summary: Optional[str]
    answer: Optional[str]
    keywords: Optional[str]

    vector_store: Optional[Any]
    retrieved_chunks: List[str]

    evaluation: Optional[str]

    action: str