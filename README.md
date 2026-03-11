# Semantic Search Engine

A simple **Semantic Search Engine** built with Django, PostgreSQL (pgvector), Azure OpenAI embeddings, and Streamlit.

The system allows users to search documents using both **keyword search** and **semantic search**.

---

## Features

Keyword Search: Finds documents using text matching  
Semantic Search: Finds documents using vector similarity  
Django REST API backend  
Streamlit UI for search interface  
PostgreSQL with pgvector for storing embeddings  
Optional caching for faster queries  

---

## Architecture

User  
↓  
Streamlit UI  
↓  
Django API  
↓  
Embedding Model (Azure OpenAI)  
↓  
PostgreSQL + pgvector  
↓  
Search Results

---

## Tech Stack

Django  
Streamlit  
PostgreSQL  
pgvector  
Azure OpenAI Embeddings  
Python  

---

## Installation

### 1. Clone repo


git clone https://github.com/yourname/semantic-search-engine.git

cd semantic-search-engine


### 2. Create virtual environment


python -m venv venv
venv\Scripts\activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Run PostgreSQL with pgvector

Example using Docker:


docker run -d
--name pgvector-db
-e POSTGRES_PASSWORD=postgres
-e POSTGRES_DB=semanticdb
-p 5432:5432
pgvector/pgvector:pg16


### 5. Run Django backend


cd backend
python manage.py migrate
python manage.py runserver


### 6. Run Streamlit UI

Open another terminal:


cd frontend
streamlit run streamlit_app.py


---

## Example

Search Query:


python programming


Semantic Search Result:


Python Basics
Python is a programming language used for AI and web development.

Django Framework
Django is a Python web framework used to build scalable applications.


---

## Workflow

User  
↓  
Streamlit UI  
↓  
Django API  
↓  
Generate Query Embedding  
↓  
pgvector Similarity Search  
↓  
Return Top Matching Documents