import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document  # Correct import for Document class

# Load the text data
with open("requirements.txt", "r") as f:
    text_data = f.read().splitlines()  # Split by lines, each line as a document

# Generate embeddings
embeddings = OpenAIEmbeddings()

# Wrap each line of text into a Document object
documents = [Document(page_content=line) for line in text_data if line.strip() != '']  # Avoid empty lines

# Check if documents are created correctly
print(f"Created {len(documents)} documents for embedding.")

# Create a FAISS index from documents and their embeddings
faiss_index = FAISS.from_documents(documents, embeddings)

# Save the FAISS index using LangChain's method
faiss_index.save_local("faiss_store")

print("FAISS index saved successfully!")
