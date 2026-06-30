from evaluator import evaluate_response


def evaluation_agent(state):

    print("📊 Evaluation Agent Running...")

    # Decide which response to evaluate
    if state["summary"]:
        response = state["summary"]

    elif state["answer"]:
        response = state["answer"]

    elif state["keywords"]:
        response = state["keywords"]

    else:
        response = "No response generated."

    # Evaluate the response
    evaluation = evaluate_response(response)

    # Save evaluation in the state
    state["evaluation"] = evaluation

    return state