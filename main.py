#Simple chatbot
def chatbot_response(user_choice):
    user_choice = user_choice.lower()

    if "hello" in user_choice or "hi" in user_choice:
        return
    
    elif "how are you" in user_choice:
        return "I'm doing great> Thank for asking."
    
    elif "your name" in user_choice:
        return "My name is Chatbot."
    
    elif "bye" in user_choice:
        return "Goodbye! have a good day."
    else:
        return " Sorry, I didn't understand that."
    
# Main Loop
print("Welcome to our Chatbot!")
print("Chatbot: Hello! Type something (type 'bye' to exit)")

while (True):
    user = input("You:")

    response = chatbot_response(user)

    print("Chatbot:", response)

    if "bye" in user.lower():
        break
    
