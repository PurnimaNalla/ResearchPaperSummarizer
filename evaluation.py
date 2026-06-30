from evaluator import evaluate_response


def evaluation_agent(state):

    print("📊 Evaluation Agent Running...")

    # Select the latest response
    if state["summary"] != "":
        response = state["summary"]

    elif state["answer"] != "":
        response = state["answer"]

    else:
        response = state["keywords"]

    # Evaluate response
    evaluation = evaluate_response(response)

    # Save in state
    state["evaluation"] = evaluation

    return state