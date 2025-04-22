from flask import Flask, jsonify, request
from flask_cors import CORS
from gemini_helper import analyze_opinion
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    topic = data.get('topic', '')
    
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
        
    try:
        analysis = analyze_opinion(topic)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({
            "error": "Analysis failed",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)