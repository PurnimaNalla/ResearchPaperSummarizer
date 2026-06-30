from tools import summarize_paper, answer_question, extract_keywords

class ResearchAgent:

    def __init__(self, vector_store, text):
        self.vector_store = vector_store
        self.text = text

    # Tool 1 - Summarize Paper
    def summarize(self):
        return summarize_paper(self.text)

    # Tool 2 - Question Answering
    def ask(self, question):
        return answer_question(self.vector_store, question)

    # Tool 3 - Keyword Extraction
    def keywords(self):
        return extract_keywords(self.text)