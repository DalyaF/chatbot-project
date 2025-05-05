document.addEventListener('DOMContentLoaded', () => {
    const chatbotContainer = document.getElementById('chatbot-container');
    const closeButton = document.getElementById('close-btn');
    const minimizeButton = document.getElementById('minimize-btn');
    const sendButton = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const chatbotMessages = document.getElementById('chatbot-messages');

    // Afficher la fenêtre chatbot immédiatement
    chatbotContainer.style.display = 'block';

    // Fonction pour afficher les messages du chatbot
    function displayMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(sender);
        messageDiv.innerText = message;
        chatbotMessages.appendChild(messageDiv);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight; // Scroll au bas
    }

    // Envoyer une question automatiquement à l'utilisateur dès que la page est chargée
    setTimeout(() => {
        displayMessage("Bonjour! Comment puis-je vous aider aujourd'hui?", 'bot');
    }, 1000);  // 1000 ms (1 seconde) après le chargement de la page

    // Gérer l'envoi de message
    sendButton.addEventListener('click', async () => {
        const message = userInput.value.trim();
        if (message) {
            displayMessage(message, 'user');
            userInput.value = ''; // Effacer le champ de texte

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message }),
                });

                const data = await response.json();
                displayMessage(data.response, 'bot');
            } catch (error) {
                console.error('Erreur:', error);
                displayMessage('Erreur de connexion. Essayez à nouveau.', 'bot');
            }
        }
    });

    // Fermer la fenêtre
    closeButton.addEventListener('click', () => {
        chatbotContainer.style.display = 'none';
    });

    // Minimiser la fenêtre
    minimizeButton.addEventListener('click', () => {
        chatbotContainer.classList.toggle('minimized');
        if (chatbotContainer.classList.contains('minimized')) {
            minimizeButton.innerText = 'Restore';
        } else {
            minimizeButton.innerText = '_';
        }
    });
});
