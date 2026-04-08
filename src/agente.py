import requests

def responder(pergunta):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": f"Você é um assistente financeiro. Responda de forma clara e simples:\n{pergunta}",
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()

    return data["response"]
