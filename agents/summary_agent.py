from tools import summarize_paper


def summary_agent(state):

    print("📑 Summary Agent Running...")

    try:
        summary = summarize_paper(state["text"])

        state["summary"] = summary

    except Exception as e:

        state["summary"] = f"Error: {str(e)}"

    return state