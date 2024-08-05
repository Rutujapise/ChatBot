import nltk
from nltk.chat.util import Chat, reflections

# Define a list of pairs containing patterns and responses
patterns_and_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you!', 'You can call me Chatbot.']),
    (r'quit', ['Goodbye!', 'Have a nice day!']),
]

# Create a chatbot instance
chatbot = Chat(patterns_and_responses, reflections)

def start_chat():
    print("Chatbot: Hi! How can I assist you today? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I’m not sure how to respond to that.")

if __name__ == "__main__":
    start_chat()
