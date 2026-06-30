def evaluate_response(response):

    score = 10
    remarks = []

    # Check response length
    if len(response) < 80:
        score -= 3
        remarks.append("Response is too short.")

    # Check hallucination
    if "I could not find" in response:
        score -= 2
        remarks.append("Information not found in uploaded paper.")

    # Check detail
    if len(response.split()) > 400:
        remarks.append("Detailed response.")

    # Overall Quality
    if score >= 8:
        quality = "Excellent"
    elif score >= 6:
        quality = "Good"
    else:
        quality = "Needs Improvement"

    return f"""
Overall Quality : {quality}

Score : {score}/10

Remarks:

{chr(10).join(remarks)}
"""