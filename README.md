# 📚 Project Overview

This repository contains two main components:

- **Backend:** FastAPI-based To-Do List API (`main.py`)
- **Frontend:** Simple web interface for interacting with the API (`frontend/`)

---

## 🗂️ Structure

```
myAPI/
├── main.py         # FastAPI backend
├── frontend/       # Frontend app (HTML/JS/CSS)
│   ├── index.html
│   └── ...
└── README.md
```

---

# 🖥️ Frontend

The frontend is a lightweight web app that lets you:

- View all to-do items
- Add new items
- view task by ID

## ▶️ Running the Frontend

1. Start the FastAPI backend (see below).
2. Open `frontend/index.html` in your browser.
3. The frontend will interact with the API at `http://localhost:8000`.

---

# ⚙️ Backend (FastAPI)

See below for backend features and requirements.

---



# 📝 FastAPI To-Do List API (In-Memory)

This is a simple, in-memory to-do list API built with **FastAPI** for learning and demonstration purposes.

## 🚀 Features

- Add new to-do items
- View all items (with optional limit)
- View a single item by ID
- In-memory storage (resets on server restart)
- Pydantic request validation
- Auto-generated docs via Swagger UI

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```
