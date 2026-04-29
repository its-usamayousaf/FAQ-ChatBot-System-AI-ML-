 🤖 FAQ Chatbot System (AI/ML Project)

This project is developed as part of the Calder AI/ML Internship selection process.


🚀 Project Overview
The FAQ Chatbot System is designed to answer user queries by retrieving the most relevant response from a predefined dataset of frequently asked questions.

The system uses Natural Language Processing (NLP) techniques to convert text into numerical vectors and applies similarity matching to find the best answer.

🎯 Objective
- Build a chatbot that responds to user queries
- Retrieve answers from a structured FAQ dataset
- Use similarity-based matching instead of hardcoded rules
- Handle unknown queries gracefully

 ✨ Features
- 📂 Structured FAQ dataset (JSON format)
- 🧠 TF-IDF based text vectorization
- 📊 Cosine similarity for matching queries
- ⚡ Fast retrieval-based response system
- ❌ Handles unmatched queries using threshold logic
- 🧩 Modular and clean code structure

 🛠️ Technologies Used
- Python
- Scikit-learn (TF-IDF, Cosine Similarity)
- JSON (for dataset storage)

📂 Project Structure

faq_chatbot/
│── data/
│ └── faq.json
│── src/
│ └── chatbot.py
│── app.py
│── requirements.txt
│── README.md
