import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_opinion(topic):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        
        prompt = f"""Analyze current public opinion about "{topic}" and return ONLY valid JSON:
        {{
            "sentiment": {{
                "positive": 60,
                "negative": 25,
                "neutral": 15
            }},
            "positive_points": ["Point 1 🚀", "Point 2 👍", "Point 3 🌍", "Point 4 🌍","Point 5 🌍"],
            "negative_points": ["Issue 1 😟", "Issue 2 👎", "Issue 3 💸","Issue 4 💸","Issue 5 💸"],
            "impact_analysis": "Summary in 150 words ...",
            "summary": "Overall conclusion...",
            "sources names": "articles and news names ",
        }}
        Requirements:
        - Return ONLY the JSON without any additional text
        - Ensure valid JSON format
        - Sentiment percentages must total 100"""
        
        response = model.generate_content(
            prompt,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
            }
        )
        
        return _parse_response(response.text)
        
    except Exception as e:
        return _error_response(str(e))

def _parse_response(text):
    try:
        # Clean and extract JSON
        json_str = text.replace('```json', '```').replace('```', '').strip()
        
        # Parse safely
        parsed = json.loads(json_str)
        
        # Validate structure
        required = ['sentiment', 'positive_points', 'negative_points']
        if not all(key in parsed for key in required):
            raise ValueError("Invalid response structure")
            
        # Validate sentiment totals
        total = sum(parsed['sentiment'].values())
        if total != 100:
            raise ValueError(f"Sentiment percentages sum to {total} instead of 100")
            
        return parsed
        
    except Exception as e:
        print(f"Raw Gemini Response:\n{text}")  # Debugging
        return _error_response(f"Parse error: {str(e)}")

def _error_response(error):
    return {
        "error": error,
        "sentiment": {"positive": 0, "negative": 0, "neutral": 0},
        "positive_points": [],
        "negative_points": [],
        "impact_analysis": "Analysis failed",
        "summary": "Please try again later"
    }