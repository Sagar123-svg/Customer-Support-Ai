# test_llama.py

from backend.llm import generate_llama_response

response = generate_llama_response(
    "My payment failed.",
    "Refunds are allowed within 30 days."
)

print(response)