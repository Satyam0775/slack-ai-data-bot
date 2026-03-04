# Slack AI Data Bot

An AI-powered Slack bot that converts natural language questions into SQL queries and retrieves results from a PostgreSQL database.
This bot allows users to ask questions about sales data directly in Slack using a slash command.

Example:
/ask-data show revenue by region for 2025-09-01

The bot automatically converts the question into SQL, executes it on PostgreSQL, and returns the results in Slack.

---

# Architecture

Slack Slash Command  
↓  
Flask API Server  
↓  
LangChain Prompt + Groq LLM  
↓  
SQL Query Generation  
↓  
PostgreSQL Database  
↓  
Formatted Result  
↓  
Slack Response

---

# Tech Stack

Python  
Flask  
LangChain  
Groq LLM  
PostgreSQL  
Slack API  
SQLAlchemy  
ngrok

---

# Project Structure
# Slack AI Data Bot

An AI-powered Slack bot that converts natural language questions into SQL queries and retrieves results from a PostgreSQL database.

This bot allows users to ask questions about sales data directly in Slack using a slash command.

Example:

/ask-data show revenue by region for 2025-09-01

The bot automatically converts the question into SQL, executes it on PostgreSQL, and returns the results in Slack.

---

# Architecture

Slack Slash Command  
↓  
Flask API Server  
↓  
LangChain Prompt + Groq LLM  
↓  
SQL Query Generation  
↓  
PostgreSQL Database  
↓  
Formatted Result  
↓  
Slack Response

---

# Tech Stack

Python  
Flask  
LangChain  
Groq LLM  
PostgreSQL  
Slack API  
SQLAlchemy  
ngrok

---

# Project Structure
slack-ai-data-bot
│
├── app
│ ├── config.py
│ ├── database.py
│ ├── formatter.py
│ ├── llm_sql.py
│ ├── main.py
│ └── slack_handler.py
│
├── prompts
│ └── sql_prompt.txt
│
├── requirements.txt
├── run.sh
├── README.md
└── .env


---

# Database Schema

Table: `public.sales_daily`

Columns:

| Column | Type |
|------|------|
| date | DATE |
| region | TEXT |
| category | TEXT |
| revenue | NUMERIC |
| orders | INTEGER |
| created_at | TIMESTAMPTZ |

---

# Example Queries

Example 1
/ask-data show revenue by region for 2025-09-01


Generated SQL

SELECT region, SUM(revenue)
FROM public.sales_daily
WHERE date = '2025-09-01'
GROUP BY region


Example 2
/ask-data total orders by region


Generated SQL

SELECT region, SUM(orders)
FROM public.sales_daily
GROUP BY region


Example 3
/ask-data revenue by category

Generated SQL

SELECT category, SUM(revenue)
FROM public.sales_daily
GROUP BY category


---

# Setup Instructions

### 1 Install Dependencies
pip install -r requirements.txt


---

### 2 Configure Environment Variables

Create `.env`

GROQ_API_KEY=your_groq_api_key
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_SIGNING_SECRET=your_slack_signing_secret
DATABASE_URL=postgresql://postgres:password@localhost:5432/analytics
PORT=3000


---

### 3 Run Server
python -m app.main


---

### 4 Start ngrok

ngrok http 3000
Use the ngrok URL for Slack command.

Example:
https://your-ngrok-url/slack/events


---

# Slack Command
/ask-data

Example:
/ask-data show revenue by region for 2025-09-01


---

# Security
The system restricts generated queries to **SELECT statements only** to prevent destructive database operations.

---

# Features
Natural Language to SQL using LLM  
Slack Slash Command Interface  
PostgreSQL Analytics Queries  
Formatted Table Responses  
Secure Query Execution  

---

# Example Output
Query Results

region sum
North 125000.50
South 54000.00
West 40500.00


---

# Author
Satyam Kumar
AI / Machine Learning Engineer