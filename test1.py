import random

# Define predefined rules and responses
greetings = ["hello", "hi", "hey", "howdy"]
farewells = ["goodbye", "bye", "see you", "take care"]
questions = ["how are you", "what's your name", "what can you do", "who created you"]
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "hey": "Hey! What can I do for you?",
    "howdy": "Howdy! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "bye": "Goodbye! Feel free to return anytime.",
    "see you": "See you later!",
    "take care": "You too, take care!",
    "how are you": "I am i'm just a computer program, so I don't have feelings, but I'm here to help!",
    "what's your name": "I'm a chatbot created by [kuki].",
    "what can you do": "I can answer your questions and assist you with various tasks.",
    "who created you": "I was created by [kuki] using Python."
}

# Main chatbot loop
while True:
    user_input = input("You: ").lower()
    
    # Check if the user's input matches any predefined rules
    if user_input in greetings:
        bot_response = responses[random.choice(greetings)]
    elif user_input in farewells:
        bot_response = responses[random.choice(farewells)]
    elif user_input in questions:
        bot_response = responses[user_input]
    else:
        bot_response = "I'm sorry, I don't understand that. Can you please rephrase or ask another question?"

    print("Bot:", bot_response)
