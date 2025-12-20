# Intelligent Book Management System (BMS)

Async Book Management System built using **FastAPI**, **PostgreSQL**, **JWT authentication**, and **local AI integration (Ollama – Llama 3.2)**.

This file contains **all instructions** required to set up, run, test, and verify the project.

---

## Prerequisites

- Python 3.10+
- PostgreSQL
- pgAdmin 4
- Ollama
- Git

---

## Setup & Run Instructions

### Create & Activate Virtual Environment

- Install Dependencies

pip install -r requirements.txt

- Create two PostgreSQL databases:

bms_db (development)

bms_test_db (testing)

- Create a .env file in project root

DATABASE_URL=postgresql+asyncpg://postgres:PASSWORD@localhost:5432/bms_db

SECRET_KEY=secure_random_key

ENV=dev

- Run Application

uvicorn app.main:app --reload

API Testing Order (Swagger)

GET /health

POST /auth/register

POST /auth/login

Click Authorize → paste JWT token only

POST /books

GET /books

GET /books/{id}

POST /books/{id}/reviews

GET /books/{id}/reviews

POST /generate-summary

GET /books/{id}/summary

DELETE /books/{id}
