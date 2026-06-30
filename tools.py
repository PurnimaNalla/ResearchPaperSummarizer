import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# ---------------------------------------------------
# Tool 1 : Summarize Research Paper
# ---------------------------------------------------

def summarize_paper(text):

    prompt = f"""
You are an AI Research Assistant.

Summarize the following research paper.

Include:

1. Overview
2. Objectives
3. Methodology
4. Key Findings
5. Conclusion

Research Paper:

{text}
"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# Tool 2 : Question Answering
# ---------------------------------------------------

def answer_question(vector_store, question):

    docs = vector_store.similarity_search(question, k=2)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are an AI Research Assistant.

Answer the question using ONLY the information provided below.

Rules:
1. Use ONLY the provided context.
2. Do NOT use external knowledge.
3. Do NOT guess.
4. If the answer is not present in the context, reply exactly:
"I could not find this information in the uploaded research paper."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# Tool 3 : Keyword Extraction
# ---------------------------------------------------

def extract_keywords(text):

    prompt = f"""
Extract the 15 most important keywords from the following research paper.

Return only the keywords as a comma-separated list.

Research Paper:

{text}
"""

    response = model.generate_content(prompt)

    return response.text