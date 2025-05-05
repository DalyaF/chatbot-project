from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Fonction pour obtenir la réponse du chatbot
def get_bot_response(user_input):
    responses = {
    "bonjour": "Bonjour! Comment puis-je vous aider?",
    "comment ça va": "Je vais bien, merci de demander!",
    "au revoir": "Au revoir! À bientôt!",
    "comment tu t'appelles": "Je suis un chatbot. Je n'ai pas de nom, mais vous pouvez m'appeler comme vous voulez!",
    "que peux-tu faire": "Je peux répondre à vos questions et vous aider avec certaines tâches simples. Que souhaitez-vous savoir?",
    "aide": "Je suis là pour vous aider. Posez-moi une question et je ferai de mon mieux pour y répondre.",
    "raconte une blague": "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant? Parce que sinon ils tombent toujours dans le bateau!",
    "quelle heure est-il": "Désolé, je ne peux pas vous dire l'heure, mais vous pouvez vérifier sur votre appareil.",
    "quel âge as-tu": "Je suis un programme informatique, donc je n'ai pas d'âge, mais merci de demander!",
    "quel temps fait-il": "Désolé, je ne peux pas vous donner la météo pour l'instant.",
    "d'où viens-tu": "Je viens d'internet! Je n'ai pas de lieu physique.",
    "tu peux m'aider avec du code": "Oui, je peux vous aider avec des questions de programmation. Que voulez-vous savoir?",
    "merci": "Avec plaisir! Si vous avez d'autres questions, n'hésitez pas à demander.",
    "bonjour le matin": "Bonjour! Comment puis-je vous aider ce matin?",
    "bonne nuit": "Bonne nuit! À demain!",
    "quelle est ta couleur préférée": "Je n'ai pas de préférence, mais j'aime bien toutes les couleurs!",
    "peux-tu faire une recherche sur google": "Désolé, je ne peux pas effectuer de recherches Google directement, mais je peux vous aider à formuler des questions."
    }

    return responses.get(user_input.lower(), "Désolé, je n'ai pas compris.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_response = get_bot_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
