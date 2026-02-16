
# 📘 Qdrant Rag

A fully local **Retrieval-Augmented Generation (RAG)** system built using:

- 🧠 TinyLlama (LLM inference via llama-cpp-python)
- 📦 Qdrant (Vector Database)
- 🔎 sentence-transformers (Embeddings)
- 🤖 OpenAI-compatible local API server

This project demonstrates how to build an end-to-end ChatGPT-style RAG pipeline completely locally.

---

## 🚀 Features

- ✅ Local LLM inference using TinyLlama
- ✅ Semantic search with Qdrant vector database
- ✅ Embedding generation using sentence-transformers
- ✅ End-to-end RAG pipeline
- ✅ Fully local execution (No external API required)

---

## 🧰 Prerequisites

| Requirement | Version |
|------------|----------|
| Python | 3.10+ |
| Docker | Installed & Running |
| Git | Installed |
| RAM | 16GB Recommended (for LLM) |

Optional:
- GPU for faster inference
- GitHub Codespaces (if not running locally)

---

# 📌 Step-by-Step Setup Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anurag-Patwegar/Qdrant_Rag.git
cd Qdrant_Rag
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Qdrant Vector Database

```bash
docker run -d -p 6333:6333 qdrant/qdrant
```

Qdrant will run on:
```
http://localhost:6333
```

---

## 5️⃣ Setup & Start LLM Server

Download a TinyLlama compatible GGUF model file and place it locally.

Start the server:

```bash
python app/server.py
```

⚠️ First startup may take a few minutes depending on system performance.

---

## 6️⃣ Document Ingestion & Embedding

Before querying:

1. Load documents  
2. Generate embeddings  
3. Store embeddings in Qdrant  

Example embedding logic:

```python
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

model = SentenceTransformer("all-mpnet-base-v2")
client = QdrantClient(host="localhost", port=6333)

# Generate embeddings and push to Qdrant
```

Run ingestion script (if available):

```bash
python ingest.py
```

---

## 7️⃣ Query the RAG System

```bash
python app/query.py "What is Retrieval Augmented Generation?"
```

Pipeline flow:

1. Convert query → embedding  
2. Retrieve relevant vectors from Qdrant  
3. Send retrieved context + query to TinyLlama  
4. Generate contextual answer  

---

# 🧪 End-to-End Execution Order

```bash
# 1. Start Qdrant
docker run -d -p 6333:6333 qdrant/qdrant

# 2. Activate environment
source venv/bin/activate   # or Windows equivalent

# 3. Start LLM server
python app/server.py

# 4. Ingest documents
python ingest.py

# 5. Run query
python app/query.py
```

---

# 📁 Project Structure

```
Qdrant_Rag/
│
├── app/                # LLM server and query logic
├── scripts/            # Utility / ingestion scripts
├── requirements.txt
├── README.md
└── docs/               # Sample documents (if provided)
```

---

# 🛠 Troubleshooting

| Issue | Solution |
|-------|----------|
| Qdrant not running | Check Docker container status |
| Port 6333 blocked | Ensure no firewall blocking |
| LLM crashes | Ensure enough RAM |
| Slow inference | Use smaller model or enable GPU |

Check running containers:

```bash
docker ps
```

Stop Qdrant:

```bash
docker stop <container_id>
```

---

# 💡 Best Practices

- Use smaller models during development  
- Use GPU acceleration if available  
- Monitor memory usage  
- Keep embeddings consistent (same model for indexing and querying)  

---

# 📜 License

No explicit license found. Refer to repository for updates.

---

# 🙌 Contributing

Contributions are welcome!

- Improve ingestion pipeline  
- Add better chunking strategies  
- Add streaming responses  
- Add frontend UI  

Feel free to raise issues or submit pull requests.

---

# 🧠 What This Project Demonstrates

- Vector databases  
- Local LLM serving  
- Semantic search  
- End-to-end RAG pipeline  
- Production-style modular architecture  

Perfect for learning LLMOps, RAG architecture, and local AI system deployment.

---

⭐ If you find this useful, consider starring the repository!
