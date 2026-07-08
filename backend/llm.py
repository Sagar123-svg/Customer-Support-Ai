import requests


def generate_llama_response(ticket, context):

    try:

        prompt = f"""
Act as a professional customer support representative.

Use the following template:

Greeting

Acknowledgement of issue

Relevant policy information

Next steps

Closing

Customer Issue:
{ticket}

Company Policy:
{context}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 80
                }
            },
            timeout=120
        )

        return response.json()["response"]

    except Exception as e:

        print("LLAMA ERROR:", e)

        return f"""
Dear Customer,

Thank you for contacting us.

{context}

Please let us know if you require further assistance.

Best Regards,
Customer Support Team
"""
    