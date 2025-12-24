# Intelligent Book Management System (BMS)

An **async, modular, and well-structured backend prototype** built using **FastAPI**, **PostgreSQL**, **JWT authentication**, and **local AI integration (Ollama + Llama 3.2)**.

---

## Key Characteristics

- Async FastAPI application

- PostgreSQL with async SQLAlchemy

- JWT authentication with role-based access control (RBAC)

- Local AI integration using Ollama

- Blocking AI calls executed safely in a threadpool

- Clear separation of concerns (routes, services, repositories, models)

- Environment-based configuration

- Strong request/response validation

- Deterministic startup behavior

---

## Technology Stack

- **Language**: Python 3.10+

- **API Framework**: FastAPI (async)

- **Database**: PostgreSQL

- **ORM**: SQLAlchemy (asyncio)

- **DB Driver**: asyncpg

- **Authentication**: JWT (python-jose)

- **Password Hashing**: bcrypt / passlib

- **AI Model**: Llama 3.2 (via Ollama)

- **AI Integration**: LangChain (sync wrapped safely)

- **Testing**: pytest, pytest-asyncio

- **Configuration**: Environment variables (.env)

---

## Database Schema

### users

- id (PK)

- email (unique, indexed)

- hashed_password

- role

### books

- id (PK)

- title (indexed)

- author (indexed)

- genre (indexed)

- year_published

- summary

### reviews

- id (PK)

- book_id (FK → books.id)

- user_id (FK → users.id)

- review_text

- rating (1–5)

---

## Prerequisites

- Python 3.10+

- PostgreSQL installed locally

- pgAdmin 4

- Ollama installed and running

- Git

---

## Environment Setup

### 1. Create virtual environment

```bash

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Create PostgreSQL databases

Using pgAdmin 4:

bms_db (development)

bms_test_db (testing)


Create .env file

DATABASE_URL=postgresql+asyncpg://postgres:PASSWORD@localhost:5432/bms_db

JWT_SECRET_KEY=your_secure_random_key_min_32_chars

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

AI_MODEL_NAME=llama3.2:1b
```

Running the Application:

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
