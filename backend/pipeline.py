from backend.classifier import predict_ticket
from backend.sentiment import analyze_sentiment
from backend.rag import retrieve_document
from backend.database import save_ticket


def generate_response(ticket, category, sentiment, document):

    response = f"""
Customer Issue Category: {category}

Sentiment: {sentiment['label']}

Relevant Information:
{document['content']}

Suggested Response:

Dear Customer,

We apologize for the inconvenience.

Based on our records and support policies:

{document['content']}

Please let us know if you need further assistance.

Best Regards,
Customer Support Team
"""

    return response


def process_ticket(ticket):

    category = predict_ticket(ticket)

    sentiment = analyze_sentiment(ticket)

    document = retrieve_document(category)
    response = generate_response(
        ticket,
        category,
        sentiment,
        document
    )
    
    save_ticket(
    ticket,
    category,
    sentiment["label"],
    document["file"],
    response
)

    
    

    escalate = False

    if sentiment["label"] == "NEGATIVE":
        escalate = True
        
    return {
        "ticket": ticket,
        "category": category,
        "sentiment": sentiment,
        "retrieved_document": document["file"],
        "escalate": escalate,
        "response": response
    }