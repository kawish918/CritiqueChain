# 🍕 Pizza Restaurant QA Bot

An interactive question-answering bot for a pizza restaurant, built using **LangChain**, **Ollama's LLMs**, and **ChromaDB**. The bot answers user questions by leveraging realistic customer reviews stored in a local vector database.

---

## ✨ Features

- Uses **LangChain** and **Ollama LLM** (`llama3`) to generate accurate, context-aware responses.
- Embeds customer reviews using the **mxbai-embed-large** model for efficient semantic search.
- Stores embedded reviews in **ChromaDB**, a local vector database.
- Retrieves the top 5 most relevant reviews per query to provide informed answers.

---

## 📦 Requirements

To run this project, you need the following Python packages:

- `langchain`
- `langchain-ollama`
- `langchain-chroma`
- `pandas`

Install all dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🧠 Local LLM Setup (Ollama)

1. Install Ollama from the official website:  
   👉 https://ollama.com/download

2. Pull the required models:

```bash
ollama pull llama3
ollama pull mxbai-embed-large
```

3. Ensure the **Ollama** service is running in the background before executing any scripts.

---

## 📁 File Structure

```
├── main.py                            # Main QA bot loop
├── vector.py                          # Embeds reviews into ChromaDB
├── realistic_restaurant_reviews.csv  # Customer review dataset
├── requirements.txt                   # Project dependencies
└── README.md                          # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/kawish918/CritiqueChain.git
cd CritiqueChain
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Create the vector database** (only needed once):

```bash
python vector.py
```

4. **Start the QA chatbot**:

```bash
python main.py
```

✅ Ask questions about the restaurant!  
💬 Type `q` to quit.

---

## 💡 Notes

- Ensure **Ollama** is running before starting any script.
- This project runs **entirely locally** with **no cloud dependencies**.

---
