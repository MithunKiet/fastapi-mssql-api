# FastAPI MSSQL API

🚀 A FastAPI-based REST API integrated with Microsoft SQL Server using **pyodbc**.  
Designed with a **clean, modular architecture** (routers → services → repositories → database).  

## Features
- MSSQL connection (Windows Authentication ready)
- API Health check (`/health`)
- Database connection check (`/health/db`)
- Application info (`/health/info`)
- User CRUD example (`/users`)

## Project Structure
mssql_api/
├─ app/
│ ├─ config.py # Configuration (env-driven)
│ ├─ database.py # DB connection handler
│ ├─ main.py # FastAPI entrypoint
│ ├─ routers/ # API routes
│ ├─ services/ # Business logic
│ ├─ repositories/ # Data access layer
│ └─ models/ # Pydantic models
└─ requirements.txt

# Quick Start Guide

1. Clone the repository: `git clone https://github.com/<your-username>/fastapi-mssql-api.git && cd fastapi-mssql-api`  
2. Create virtual environment: `python -m venv .venv`  
3. Activate environment: `.venv\Scripts\activate` (Windows) / `source .venv/bin/activate` (Linux/Mac)  
4. Install dependencies: `pip install -r requirements.txt`  
5. Create `.env` file with:  
   - `DB_DRIVER=ODBC Driver 17 for SQL Server`  
   - `DB_SERVER=MITHUNSINGH`  
   - `DB_DATABASE=TestDB`  
   - `DB_AUTH=windows`  
6. Run server: `uvicorn app.main:app --reload --port 8000`  
7. Open Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
8. Health check endpoint: `/health` → returns `{"status": "ok"}`  
9. DB connection endpoint: `/health/db` → returns `{connected: true, server_time: ...}`  
10. App info endpoint: `/health/info` → returns app name, version, env, db details  
11. User endpoints: `/users/` (list), `/users/{id}` (get by id), `POST /users/` (create user)  
12. Project structure follows clean architecture: `routers → services → repositories → database → models`  
13. Requirements: Python 3.10+, FastAPI, Uvicorn, pyodbc, MSSQL ODBC Driver (17/18)  
 

