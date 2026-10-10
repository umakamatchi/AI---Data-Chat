# Text to SQL Chatbot
An AI-powered Text-to-SQL chatbot that allows users to ask questions about an orders PostgreSQL database using natural language.

The application uses Google Gemini to convert plain-English questions into SQL queries, executes the generated queries against PostgreSQL, and displays the results through an interactive Streamlit chat interface.

The goal of this project is to demonstrate how Generative AI can provide a natural-language interface to structured business data, allowing users to interact with databases without needing to write SQL manually.
Traditional database querying requires users to understand SQL syntax.

This project provides a conversational interface where users can ask questions such as:

"What are the top 5 customers by sales?"

"Which category generated the highest profit?"

"Show me monthly sales for 2025."

"Which products have negative profit?"

The application automatically:

User Question
      ↓
Streamlit Chat Interface
      ↓
Google Gemini LLM
      ↓
SQL Generation
      ↓
SQL Validation / Safety Check
      ↓
PostgreSQL
      ↓
Query Results
      ↓
Streamlit Data Display

✨ Features

💬 Ask questions about the orders table using natural language

🤖 Generate PostgreSQL SQL using Google Gemini

🗄️ Connect directly to PostgreSQL

🔍 Retrieve database schema information

🧠 Provide schema context to the LLM for SQL generation

🔐 Restrict generated queries to read-only SQL

📊 Display query results in a Streamlit dataframe

🛠️ Tech Stack

Technology- Purpose

Python-Application development

Google Gemini- Natural-language-to-SQL generation

PostgreSQL- Database

Streamlit- Chat application UI

Pandas- Query result processing

Psycopg- PostgreSQL connection

python-dotenv- Environment variable management

📂 Project Structure

text-to-sql-orders-chatbot/


├── demo_streamlit.py       # Main Streamlit chatbot application

├── demo.py                 # Alternative application script

├── mydb.py                 # PostgreSQL connection and query helpers

├── req.txt                 # Python dependencies

├── .env                    # API/database credentials (not committed)

├── .gitignore              # Files excluded from Git

└── README.md               # Project documentation

Installation

1. Clone the repository

git clone <your-repository-url>
cd <repository-directory>

2. Create a virtual environment

Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r req.txt

🔐 Configuration

Create a .env file in the project directory.

GEMINI_API_KEY=your_gemini_api_key

Configure the PostgreSQL connection in mydb.py using your own database credentials.

For example:

host="localhost"
port=5432
database="postgres"
user="postgres"
password="your_password"

⚠️ Important

Never commit API keys or database passwords to GitHub.

Add .env to .gitignore:

.env

.venv/

__pycache__/

*.pyc

▶️ Run the Application

From the project directory:

streamlit run demo_streamlit.py

The terminal will display a local URL.

Open the URL in your browser and start asking questions about your orders data.
























📝 Display the generated SQL for transparency and debugging
💾 Maintain conversation history using Streamlit session state
🔑 Store API credentials using environment variables
