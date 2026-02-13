from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
import uuid

client = QdrantClient(host="localhost", port=6333)

collection_name = "wine_collection"

if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Catena Zapata Argentino Vineyard Malbec 2004 is bold and structured.",
    "Bodega Colome Altura Maxima Malbec 2012 is elegant and complex.",
    "Adrianna Vineyard Malbec 2004 offers deep blackberry notes."
]

points = []

for doc in documents:
    vector = model.encode(doc).tolist()
    points.append(
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"text": doc}
        )
    )

client.upsert(collection_name=collection_name, points=points)

print("Documents indexed successfully!")
