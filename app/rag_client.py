from openai import OpenAI
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# UPDATE THIS
BASE_URL = "https://YOUR-CODESPACE-URL-9000.app.github.dev/v1"

COLLECTION_NAME = "wine_collection"

client = OpenAI(
    base_url=BASE_URL,
    api_key="sk-no-key-required"
)

qdrant = QdrantClient(host="localhost", port=6333)
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

query = "Suggest me an amazing Malbec from Argentina"

query_vector = embed_model.encode(query).tolist()

search_results = qdrant.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_vector,
    limit=2
)

context = "\n".join([hit.payload["text"] for hit in search_results])

completion = client.chat.completions.create(
    model="tinyllama",
    messages=[
        {"role": "system", "content": "You are a wine expert."},
        {
            "role": "user",
            "content": f"Answer the question using this context:\n{context}\n\nQuestion: {query}"
        }
    ]
)

print(completion.choices[0].message.content)
