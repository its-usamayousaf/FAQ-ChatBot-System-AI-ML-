import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQChatbot:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.data = json.load(f)

        self.questions = [item["question"] for item in self.data]
        self.answers = [item["answer"] for item in self.data]

        # TF-IDF Vectorization
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.X = self.vectorizer.fit_transform(self.questions)

    def get_response(self, user_query):
        user_vec = self.vectorizer.transform([user_query])
        similarity = cosine_similarity(user_vec, self.X)

        max_score = similarity.max()
        index = similarity.argmax()

        # Threshold handling (IMPORTANT)
        if max_score < 0.3:
            return "Sorry, I couldn't find a relevant answer."

        return self.answers[index]