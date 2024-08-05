import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Initialize the stemmer
stemmer = PorterStemmer()

def tokenize_and_stem(sentence):
    tokens = word_tokenize(sentence.lower())
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Define patterns and responses with stemming applied
patterns_and_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you!', 'You can call me Chatbot.']),
    (r'quit', ['Goodbye!', 'Have a nice day!']),
]

def match_pattern(user_input):
    tokens = tokenize_and_stem(user_input)
    for pattern, responses in patterns_and_responses:
        pattern_tokens = tokenize_and_stem(pattern)
        if any(token in tokens for token in pattern_tokens):
            return responses
    return ["I’m not sure how to respond to that."]

def start_chat():
    print("Chatbot: Hi! How can I assist you today? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        responses = match_pattern(user_input)
        print(f"Chatbot: {responses[0]}")

if __name__ == "__main__":
    start_chat()
