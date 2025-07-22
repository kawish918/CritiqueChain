# Vector search is a databse; its gonna be hosted locally on our
# own computer using something called ChromaDB
# quickly look up relevant information that we can then pass to 
# our model
"""
This script sets up a local vector database for restaurant reviews using ChromaDB and LangChain.
It reads review data from a CSV file, generates embeddings for each review using OllamaEmbeddings,
and stores them in a persistent Chroma vector store. If the database does not exist, it adds the
documents to the store. The script also creates a retriever to fetch the top 5 most relevant reviews
based on vector similarity.
Modules:
    - langchain_ollama: For generating text embeddings.
    - langchain_chroma: For managing the Chroma vector store.
    - langchain_core.documents: For document structure.
    - os: For file system operations.
    - pandas: For reading CSV data.
Variables:
    - df: DataFrame containing restaurant reviews.
    - embeddings: Embedding function using Ollama.
    - db_location: Path to the local ChromaDB directory.
    - add_documents: Boolean indicating if documents should be added to the store.
    - documents: List of Document objects to be stored.
    - ids: List of unique document IDs.
    - vector_store: Chroma vector store instance.
    - retriever: Retriever object for querying relevant reviews.
"""


from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Number of relevant documents to retrieve
)

