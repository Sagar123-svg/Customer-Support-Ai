from backend.vector_rag import retrieve_document

query = "I want my money back"

result = retrieve_document(query)

print(result)