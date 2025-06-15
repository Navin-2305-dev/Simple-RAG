
# 🧠 Simple RAG System using Cosine Similarity & Local LLM

This project is a **Retrieval-Augmented Generation (RAG)** system that recommends user activities based on their natural language query. It retrieves the most relevant activities from a predefined corpus using **cosine similarity** and then generates a recommendation using a **locally hosted LLM** (such as [Ollama](https://ollama.com/)).

---

## 🚀 Features

- Token-level **cosine similarity** matching between query and document corpus
- Ranking of activity suggestions based on semantic similarity
- Integration with **local LLM (e.g., Mistral)** via HTTP API for generating natural language responses
- Streamed LLM output handling for dynamic response building

---

## 🛠️ Requirements

- Python 3.7+
- [Ollama](https://ollama.com/) or any local LLM server running on `http://localhost:11434`
- Python libraries:
  - `requests`
  - `math`
  - `collections`
  - `json`

Install required packages:

```bash
pip install requests
```

---

## 🧪 How It Works

1. **User Input**: The user enters a query describing what they want to do.
2. **Cosine Similarity**: The script compares the user query with a predefined list of activities using cosine similarity.
3. **Top Matches**: It selects the top 3 most similar activities.
4. **LLM Prompting**: These top matches are passed to a local LLM (e.g., Mistral) with a prompt to generate a tailored recommendation.
5. **Streamed Response**: The LLM’s response is streamed and printed in real-time.

---

## 🧠 Cosine Similarity Function

The script uses `Counter` from `collections` to tokenize and count term frequency, and calculates cosine similarity using:

```python
similarity = dot_product / (query_magnitude * document_magnitude)
```

---

## ⚙️ API Configuration

Make sure a local LLM server (like Ollama) is running:

```bash
ollama run mistral
```

Ensure it's accessible at `http://localhost:11434/api/generate`.

---

## 🧰 Customization

- ✏️ You can modify the `corpus` list to include more domain-specific activities.
- 🧠 Change the model name in the request payload to use a different LLM.
- 📜 Adjust the `prompt` to tailor response tone or structure.

---
