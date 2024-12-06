document.getElementById('send-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value.trim();
    const chatLog = document.getElementById('chat-log');

    if (!userInput) return;

    // Display user's message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user';
    userMessageDiv.textContent = userInput;
    chatLog.appendChild(userMessageDiv);

    document.getElementById('user-input').value = '';

    try {
        // Send query to the backend
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: userInput })
        });
        const data = await response.json();

        // Display assistant's response
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'message agent';
        botMessageDiv.textContent = data.response || 'No response.';
        chatLog.appendChild(botMessageDiv);
    } catch (error) {
        console.error('Error:', error);
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.className = 'message agent';
        errorMessageDiv.textContent = 'Error communicating with the server.';
        chatLog.appendChild(errorMessageDiv);
    }

    chatLog.scrollTop = chatLog.scrollHeight;
});
