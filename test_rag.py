from backend.rag import retrieve_document

query = "How can I get a refund?"

result = retrieve_document(query)

print(result)