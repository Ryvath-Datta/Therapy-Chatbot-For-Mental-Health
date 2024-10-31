# app.py
from flask import Flask, render_template, request, jsonify
from chatbot.api_handler import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_message = request.json.get("message")
    bot_response = generate_response(user_message)
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
