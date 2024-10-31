// static/script.js
async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    document.getElementById("user-input").value = "";

    const userHtml = `<div class="user-message">${userInput}</div>`;
    document.getElementById("chat-box").innerHTML += userHtml;

    const response = await fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    });
    
    const data = await response.json();
    const botHtml = `<div class="bot-message">${data.response}</div>`;
    document.getElementById("chat-box").innerHTML += botHtml;
    
    document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;
}
