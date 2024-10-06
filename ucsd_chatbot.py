from flask import Flask, request, jsonify, render_template
from groq import Groq
import os


app = Flask(__name__)

with open('local-data/info', 'r') as file:
    API_KEY = file.readline().strip()

client = Groq(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Answer the following question related to UCSD: {user_message}",
            }
        ],
        model="llama3-8b-8192",
    )

    response_message = chat_completion.choices[0].message.content
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)