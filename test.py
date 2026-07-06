from backend.classifier import predict_ticket

ticket = "I want my money back"

result = predict_ticket(ticket)

print("Predicted Category:", result)