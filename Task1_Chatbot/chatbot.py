# Rule-Based Chatbot for CodSoft AI Internship
# Responds with meaningful answers for common user queries

def chatbot():
    print("ChatBot: Hello! I am CodSoft AI Chatbot.")
    print("ChatBot: Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print("ChatBot: Hello! How can I help you?")

        # Identity questions
        elif "who are you" in user_input:
            print("ChatBot: I am a rule-based AI chatbot created for the CodSoft internship.")

        elif "what about you" in user_input:
            print("ChatBot: I am doing well and always ready to help you!")

        elif "your name" in user_input:
            print("ChatBot: My name is CodSoft AI Chatbot.")

        # Feelings
        elif "how are you" in user_input:
            print("ChatBot: I am doing great! Thank you for asking.")

        # Internship related
        elif "internship" in user_input:
            print("ChatBot: This is an Artificial Intelligence internship offered by CodSoft.")

        # Help
        elif "help" in user_input:
            print("ChatBot: You can ask me about the internship, my role, or general questions.")

        # Exit
        elif "exit" in user_input or "bye" in user_input:
            print("ChatBot: Goodbye! Have a great day.")
            break

        # Fallback (still meaningful)
        else:
            print("ChatBot: That's an interesting question. Could you please be more specific?")

if __name__ == "__main__":
    chatbot()
