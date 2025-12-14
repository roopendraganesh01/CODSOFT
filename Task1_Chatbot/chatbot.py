# Rule-Based Chatbot for CodSoft AI Internship
# Task 1: Chatbot with predefined responses

def chatbot():
    print("ChatBot: Hello! I am CodSoft AI Chatbot.")
    print("ChatBot: Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("ChatBot: Hello! How can I help you today?")

        elif "your name" in user_input:
            print("ChatBot: I am a rule-based chatbot created for the CodSoft AI Internship.")

        elif "internship" in user_input:
            print("ChatBot: This is an Artificial Intelligence internship at CodSoft.")

        elif "help" in user_input:
            print("ChatBot: You can ask about the internship, my name, or say hello.")

        elif "bye" in user_input or "exit" in user_input:
            print("ChatBot: Goodbye! Have a great day.")
            break

        else:
            print("ChatBot: Sorry, I did not understand that. Please try again.")

if __name__ == "__main__":
    chatbot()
