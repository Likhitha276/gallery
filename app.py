from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import os

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Retrieve your OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OpenAI API Key is not set in the environment variables.")

print(openai_api_key)
print('/n')

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gallery and Chat</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <script src="/static/script.js" defer></script>
    </head>
    <body>
        <div class="gallery">
            <img src="/static/painting.jpg" alt="Gallery Image">
            <div>
                <h2>MIAMI BEACH</h2>
                <p>Original on Canvas</p>
                <p>Size: 5' x 8'</p>
            </div>
        </div>
        <div class="chat-container">
            <header class="chat-header">
                <h1>BOT</h1>
            </header>
            <main class="chat-log" id="chat-log">
                <!-- Chat messages will be dynamically added here -->
            </main>
            <footer class="chat-footer">
                <textarea id="user-input" placeholder="Type a message here..." rows="1"></textarea>
                <button id="send-button">Send</button>
            </footer>
        </div>
    </body>
    </html>
    """

@app.post("/query")
async def query(request: Request):
    try:
        data = await request.json()
        query = data.get("query")

        if not query:
            return JSONResponse(content={"response": "Query is empty."}, status_code=400)

        # Create an OpenAI thread and run the assistant
        client = OpenAI(api_key=openai_api_key)
        assistant = client.beta.assistants.retrieve("asst_tO5ZZlAKF1ogX81dyrPH1Lqn")
        thread = client.beta.threads.create()

        # Create a user message
        message = client.beta.threads.messages.create(
        #assistant_id = assistant.id,
        thread_id=thread.id,
        role="user",
        content=query
        )
        #print(message)
        # Run the assistant and poll for the result
        run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        )

        if run.status == 'completed':
            # Fetch messages and find assistant response
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            assistant_message = next(
                (m.content[0].text.value for m in messages if m.role == "assistant"), 
                "No response from assistant."
            )
            return JSONResponse(content={"response": assistant_message})

        return JSONResponse(content={"response": f"Run status: {run.status}"})

    except Exception as e:
        return JSONResponse(content={"response": f"Error occurred: {str(e)}"}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
