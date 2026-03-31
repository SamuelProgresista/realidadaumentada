from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    r = requests.post(
        'https://api.anthropic.com/v1/messages',
        headers={
            'x-api-key': 'TU_API_KEY_AQUI',
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json'
        },
        json=request.json
    )
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(port=5001)