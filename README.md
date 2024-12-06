This is a FastAPI-based web application that integrates a gallery display with a chatbot powered by OpenAI's API. The application allows users to explore an art gallery and interact with a chatbot for personalized responses.

Features
Gallery Section: Displays an artwork with its description.
Chatbot Integration: Provides interactive chat functionality.
Static Assets: Includes static files for styling and scripts.
OpenAI Integration: Uses OpenAI's API for generating chatbot responses.

Prerequisites
Before you can run this application, ensure you have the following installed:
Python 3.11+
Virtual environment tools (e.g., venv, pipenv)
An OpenAI API key

Gallery and Chat Application
This is a FastAPI-based web application that integrates a gallery display with a chatbot powered by OpenAI's API. The application allows users to explore an art gallery and interact with a chatbot for personalized responses.

Features
Gallery Section: Displays an artwork with its description.
Chatbot Integration: Provides interactive chat functionality.
Static Assets: Includes static files for styling and scripts.
OpenAI Integration: Uses OpenAI's API for generating chatbot responses.

Prerequisites:
Before you can run this application, ensure you have the following installed:
Python 3.11+
Virtual environment tools (e.g., venv, pipenv)
An OpenAI API key

Setup Instructions:
Clone the Repository
git clone https://github.com/<your-username>/<repository>.git  
cd <repository>  

Install Dependencies:
python -m venv env  
source env/bin/activate  # On Windows: env\Scripts\activate  
pip install -r requirements.txt 

 Set OpenAI API Key
Create a .env file:
OPENAI_API_KEY=your_openai_api_key  

Run the App
uvicorn main:app --reload  

Visit: http://127.0.0.1:8000

Project Structure
├── main.py                 # Main application script
├── static/
│   ├── styles.css          # Stylesheet for the application
│   ├── script.js           # JavaScript for chat functionality
│   ├── painting.jpg        # Example gallery image
├── templates/              # HTML templates (if applicable)
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
