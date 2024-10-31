# chatbot/api_handler.py

import google.generativeai as genai
import os

# Initialize the API with the provided key
api_key = "AIzaSyBhTENggWikuXTxQODjHIrVODNwtKl53Do"  # Directly set API key here for demonstration
genai.configure(api_key=api_key)

def generate_response(prompt):
    """
    Generates a response from Google Gemini API based on user input.
    
    Args:
        prompt (str): User input message.
        
    Returns:
        str: Generated response from the API or an error message if the request fails.
    """
    try:
        # Specify the model name and prompt for generation
        model = genai.GenerativeModel('gemini-pro')  # Initialize the model here
        response = model.generate_content(prompt)  # Use generate_content method instead
        return response.text  # Access the generated response
    except Exception as e:
        print(f"Error encountered: {e}")  # Log the specific error to console
        return "I'm here to help, but I ran into an issue processing your message."

def main():
    """
    Main function to run a simple command-line interface for testing the response generation.
    """
    print("Welcome to the Therapy Chatbot for Mental Health.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for chatting. Take care!")
            break
        
        response = generate_response(user_input)
        print(f"Chatbot: {response}\n")

# Example usage if you want to test this file independently
if __name__ == "__main__":
    main()
