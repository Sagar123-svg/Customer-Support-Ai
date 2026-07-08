# 🤖 AI Customer Support Automation System

## 📖 Overview

An AI-powered Customer Support Automation System built using FastAPI, Streamlit, SQLite, Machine Learning, NLP, and Retrieval-Augmented Generation (RAG).

The application automatically:

- Classifies customer support tickets
- Detects customer sentiment
- Retrieves relevant knowledge base documents
- Generates automated responses
- Escalates negative tickets
- Tracks ticket history
- Provides analytics dashboards
- Supports CSV report exports

---

# 🚀 Features

## Ticket Classification

Automatically categorizes support requests into:

- Billing
- Shipping
- Technical

---

## Sentiment Analysis

Detects customer sentiment:

- Positive
- Neutral
- Negative

---

## Escalation Logic

Negative tickets are automatically flagged for escalation.

---

## RAG (Retrieval-Augmented Generation)

Retrieves information from:

- refund_policy.txt
- shipping_policy.txt
- technical_faq.txt

---

## AI Response Generation

Generates support responses using retrieved company knowledge.

---

## Ticket History

Stores:

- Ticket
- Category
- Sentiment
- Retrieved Document
- Response
- Timestamp

---

## Analytics Dashboard

Provides:

- Total Tickets
- Category Distribution
- Escalated Tickets
- Bar Chart Analytics
- Pie Chart Analytics

---

## Search and Filters

Search tickets using keywords and filter by:

- Category
- Sentiment

---

## CSV Export

Export ticket reports for business reporting and analysis.

---

# 🏗️ Project Architecture

```text
Customer
    │
    ▼
Streamlit Dashboard
    │
    ▼
FastAPI Backend
    │
    ▼
Ticket Classification
    │
    ▼
Sentiment Analysis
    │
    ▼
RAG Retrieval
    │
    ▼
Response Generation
    │
    ▼
SQLite Database
    │
    ▼
Analytics Dashboard
```

---

# 🔄 Workflow

```text
Customer Ticket
       │
       ▼
Ticket Classification
       │
       ▼
Sentiment Detection
       │
       ▼
Document Retrieval
       │
       ▼
Response Generation
       │
       ▼
Store in Database
       │
       ▼
Dashboard Analytics
```

---

# 📂 Project Structure

```text
Customer-Support-Ai
│
├── backend/
│   ├── classifier.py
│   ├── sentiment.py
│   ├── rag.py
│   ├── vector_rag.py
│   ├── database.py
│   ├── pipeline.py
│   └── main.py
│
├── data/
│   └── tickets.csv
│
├── knowledge_base/
│   ├── refund_policy.txt
│   ├── shipping_policy.txt
│   └── technical_faq.txt
│
├── scripts/
│
├── tests/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```
# 📊 Dashboard Screenshots

## Main Dashboard

images/dashboard.png

---

## AI Generated Response

!AI Response

---

## Ticket History

images/ticket_history.png

---

## Analytics Dashboard

images/analytics.png
---

# 🛠️ Technology Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## Database

- SQLite

## Machine Learning

- Scikit-learn

## NLP

- TextBlob

## Data Analysis

- Pandas

## Visualization

- Matplotlib

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
```

```bash
cd Customer-Support-Ai
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn backend.main:app --reload
```

## Run Streamlit

```bash
streamlit run app.py
```

---

# 📊 Dashboard Screenshots

## Main Dashboard

(Add screenshot here)

## Ticket History

(Add screenshot here)

## Analytics Charts

(Add screenshot here)

---

# 💼 Resume Highlights

### AI Customer Support Automation System

- Developed an end-to-end AI-powered customer support platform using FastAPI, Streamlit, SQLite, and Machine Learning.
- Implemented ticket classification, sentiment analysis, retrieval-augmented generation (RAG), automated response generation, escalation workflows, analytics dashboards, and CSV reporting.
- Built interactive visualizations using Pandas and Matplotlib.
- Designed persistent ticket history tracking and operational analytics for support teams.

---

# 🔮 Future Enhancements

- FAISS Vector Search
- Ollama + Llama 3 Integration
- Docker Support
- Cloud Deployment
- Advanced Analytics

---

# 👨‍💻 Author

**Saurav Shimare**