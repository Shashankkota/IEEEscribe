
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-1.5-flash"  # Use "gemini-1.5-flash" for free, fast text generation
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"

# Generate a section using Gemini API
def generate_section_gemini(prompt: str) -> str:
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(GEMINI_URL, json=data)
    if response.status_code == 200:
        candidates = response.json().get("candidates", [])
        if candidates and "content" in candidates[0]:
            return candidates[0]["content"]["parts"][0]["text"]
        else:
            return "ERROR: No content returned from Gemini API."
    else:
        return f"ERROR: Gemini API {response.status_code}: {response.text}"
