# app.py
from flask import Flask, render_template, request, jsonify
from chatbot.api_handler import generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Print the incoming request data for debugging
    print(f"Request data: {request.data}")  # Log raw data
    print(f"Request JSON: {request.json}")  # Log parsed JSON data

    user_input = request.json.get('user_input')  # Use .get() to avoid KeyError
    if user_input is None:
        return jsonify({'response': "No input provided."}), 400  # Handle missing input

    response_text = generate_response(user_input)  # Call the generate_response function
    return jsonify({'response': response_text})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
