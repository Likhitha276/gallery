import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import openai
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
# Initialize FastAPI app
app = FastAPI()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable for security

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Load FAISS index
faiss_index = None
faiss_store_path = 'faiss_store'

try:
    faiss_index = FAISS.load_local(faiss_store_path, embeddings)
    print("FAISS index loaded successfully.")
except Exception as e:
    print(f"Error loading FAISS index: {e}")

# Define gallery exhibits
gallery_exhibits = [
    {"id": 1, "name": "Modern Art Exhibit", "description": "Explore contemporary art.", "url": "/chatbox/1"},
    {"id": 2, "name": "Sculpture Showcase", "description": "Discover stunning sculptures.", "url": "/chatbox/2"},
]

# Route for querying FAISS index
@app.post("/query/")
async def query_index(query: str):
    if faiss_index is None:
        raise HTTPException(status_code=500, detail="FAISS index not loaded.")
    
    # Generate embedding for the query
    query_embedding = embeddings.embed_query(query)
    
    # Perform similarity search
    try:
        results = faiss_index.similarity_search_by_vector(query_embedding, k=1)
        most_relevant_doc = results[0].page_content  # Retrieve the document content
        return JSONResponse(content={"query": query, "response": most_relevant_doc})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during similarity search: {e}")

# Route to list gallery exhibits
@app.get("/exhibits/")
async def list_exhibits():
    return JSONResponse(content=gallery_exhibits)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
