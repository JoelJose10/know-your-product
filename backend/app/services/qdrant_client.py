from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "product_docs"
VECTOR_SIZE = 1536  # OpenAI embedding size

def get_qdrant_client():
    return QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def init_collection():
    client = get_qdrant_client()

    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )
