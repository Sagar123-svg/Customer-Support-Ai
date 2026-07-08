# test_ollama.py

import requests

print("Sending request...")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "Say Hello in one sentence.",
        "stream": False
    },
    timeout=120
)

print("Status:", response.status_code)

data = response.json()

print("\nResponse:\n")
print(data["response"])