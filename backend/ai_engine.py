import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "dolphin-phi:latest"

def get_ai_response(message: str):
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": message,
                "stream": False
            }
        )

        data = res.json()
        return data.get("response", "No response from model")

    except Exception as e:
        return f"AI Error: {str(e)}"
