def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def start_chatbot():
    print("Chatbot started! Type 'bye' to exit.")
    while True:
        user_message = input("You: ")
        response = get_bot_response(user_message)
        print(f"Bot: {response}")
        if response == "Goodbye!":
            break

start_chatbot()
