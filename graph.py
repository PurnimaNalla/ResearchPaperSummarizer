from langgraph.graph import StateGraph, END
from evaluation import evaluation_agent
from state import ResearchState

from agents.pdf_agent import pdf_agent
from agents.summary_agent import summary_agent
from agents.qa_agent import qa_agent
from agents.keyword_agent import keyword_agent
from evaluation import evaluation_agent
from agents.evaluation_agent import evaluation_agent

# Create Graph
builder = StateGraph(ResearchState)

# Add Nodes
builder.add_node("pdf", pdf_agent)
builder.add_node("summary", summary_agent)
builder.add_node("qa", qa_agent)
builder.add_node("keywords", keyword_agent)
builder.add_node("evaluation", evaluation_agent)
builder.add_node("evaluation", evaluation_agent)

# ----------------------------
# Router Function
# ----------------------------

def router(state):

    action = state["action"]

    if action == "summary":
        return "summary"

    elif action == "qa":
        return "qa"

    elif action == "keywords":
        return "keywords"

    return END


# Entry Point
builder.set_entry_point("pdf")

# After PDF Agent, decide where to go
builder.add_conditional_edges(
    "pdf",
    router,
    {
        "summary": "summary",
        "qa": "qa",
        "keywords": "keywords",
    }
)

# Finish after each agent
builder.add_edge("summary", END)
builder.add_edge("qa", END)
builder.add_edge("keywords", END)
builder.add_edge("keywords", "evaluation")
builder.add_edge("evaluation", END)
builder.add_edge("keywords", "evaluation")
builder.add_edge("evaluation", END)
builder.add_edge("keywords", "evaluation")
builder.add_edge("evaluation", END)
graph = builder.compile()