from src.chatbot import FAQChatbot

bot = FAQChatbot("data/faq.json")

print("🤖 FAQ Chatbot (type 'exit' to quit)")

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = bot.get_response(query)
    print("Bot:", response)