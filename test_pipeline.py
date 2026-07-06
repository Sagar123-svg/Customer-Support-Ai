from backend.pipeline import process_ticket

ticket = "My payment failed and I want a refund immediately."

result = process_ticket(ticket)

print(result["response"])