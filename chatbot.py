def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize input to lowercase

    # Define responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking! How can I assist you?"
    elif "your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the chatbot! Type 'bye' or 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if response == "Goodbye! Have a great day!":
            break

if __name__ == "__main__":
    main()