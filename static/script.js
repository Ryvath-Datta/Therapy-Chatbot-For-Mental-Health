// static/script.js
function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return; // Don't send empty messages

    // Append user message to chat box
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div>You: ${userInput}</div>`;
    
    // Clear the input field
    document.getElementById('user-input').value = '';

    // Send user input to the server
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput }) // Ensure this is structured correctly
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Append chatbot response to chat box
        chatBox.innerHTML += `<div>Chatbot: ${data.response}</div>`;
        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
