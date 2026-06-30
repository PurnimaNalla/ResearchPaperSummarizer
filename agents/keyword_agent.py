from tools import extract_keywords


def keyword_agent(state):

    print("🔑 Keyword Agent Running...")

    try:
        keywords = extract_keywords(state["text"])

        state["keywords"] = keywords

    except Exception as e:

        state["keywords"] = f"Error: {str(e)}"

    return state