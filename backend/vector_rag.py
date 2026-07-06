import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
texts = []

knowledge_path = "knowledge_base"

for file in os.listdir(knowledge_path):

    with open(
        os.path.join(knowledge_path, file),
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

        documents.append({
            "file": file,
            "content": content
        })

        texts.append(content)

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings, dtype=np.float32))


def retrieve_document(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding, dtype=np.float32),
        k=1
    )

    return documents[indices[0][0]]