# UCSD ChatBot

UCSD ChatBot is a simple web-based chatbot designed to answer UCSD-related questions. This project uses Python's Flask framework for the backend and HTML/CSS for the frontend. The bot communicates through a conversational interface, providing users with answers to various questions about UC San Diego.

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/2273565c-e8d7-46d3-8658-3c0cdab8e2f3">

## Features

- Conversational interface for UCSD-related queries
- Chat window styled using UCSD colors (blue and gold)
- Customizable backend logic for answering questions
- Responsive design with a chat-like experience

## Prerequisites

To run this project, you will need the following installed:

- Python 3.x
- `pip` (Python package installer)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Maanasa64/UCSD-ChatBot.git
   cd UCSD-ChatBot

2. **Install dependencies:**

   Use pip to install the necessary Python packages listed in requirements.txt:
   
   `pip install -r requirements.txt`

4. **Add your API Key:**

   Refer to https://console.groq.com/docs/quickstart#create-an-api-key.
   
   Add your key as an environment variable by running:
   
   `export API_KEY='your-api-key-here'`

   Optional: To make it easier to manage your environment variables, you can use `direnv`. This tool allows you to automatically set environment variables when you enter a specific          directory.


6. **Run the application:**

   You can run the app locally using Flask's built-in development server:
   
   `python ucsd_chatbot.py`

   The app should now be running locally.

