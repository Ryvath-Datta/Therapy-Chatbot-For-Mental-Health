# chatbot/api_handler.py

import google.generativeai as genai

# Initialize the API with the provided key
genai.configure(api_key="AIzaSyARiM861r4SJGoT1kD_boaIZnU5IWOtGbA")

def generate_response(prompt):
    """
    Generates a response from Google Gemini API based on user input.
    Args:
        prompt (str): User input message.
    Returns:
        str: Generated response from the API.
    """
    try:
        response = genai.generate(prompt=prompt)
        return response.generations[0].text  # Access the first generated response
    except Exception as e:
        return "I'm here to help, but I ran into an issue processing your message."
