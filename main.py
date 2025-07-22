from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

# What we want the model to do
template = """
You are an expert in answering questions about a pizza restaurant

Here are some reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n----------------------------------------------")
    question = input("Ask your question (q to quit):")
    print("\n\n")
    if question == "q":
        break
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)


# This script sets up a conversational agent for answering questions about a pizza restaurant using LangChain and OllamaLLM.
# It retrieves relevant reviews based on user questions and generates expert answers.
# Modules:
#     - langchain_ollama.llms: Provides the OllamaLLM language model interface.
#     - langchain_core.prompts: Used for creating chat prompt templates.
#     - vector: Contains the retriever for fetching relevant reviews.
# Workflow:
#     1. Initializes the OllamaLLM model.
#     2. Defines a prompt template for the model, including reviews and user questions.
#     3. Sets up a chain combining the prompt and model.
#     4. Enters a loop to interactively accept user questions.
#     5. Retrieves relevant reviews using the retriever.
#     6. Invokes the chain to generate and print answers.
#     7. Exits when the user inputs 'q'.
# Usage:
#     Run the script and enter questions about the pizza restaurant. Type 'q' to quit.