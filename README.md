# Spaetirun - FastAPI + Vue.js Application

A full-stack web application using FastAPI, SQLAlchemy ORM, PostgreSQL, and Vue.js.

## Project Structure

```
spaetirunneu/
├── backend/
│   ├── app/
│   │   ├── crud/          # Database operations
│   │   ├── models/        # SQLAlchemy models
│   │   ├── routes/        # API endpoints
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── config.py      # Configuration
│   │   ├── database.py    # Database setup
│   │   └── main.py        # FastAPI app
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/           # API client
│   │   ├── components/    # Vue components
│   │   ├── views/         # Vue views
│   │   ├── router/        # Vue Router
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── docker-compose.yml
```

## Setup Instructions

### 1. Start PostgreSQL Database

```bash
docker-compose up -d
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Backend will be available at: http://localhost:8000
API docs: http://localhost:8000/docs

### 4. Setup Frontend

```bash
cd frontend
npm install
```

### 5. Run Frontend

```bash
cd frontend
npm run dev
```

Frontend will be available at: http://localhost:5173

## Features

- FastAPI backend with automatic OpenAPI documentation
- SQLAlchemy ORM for database operations
- PostgreSQL database
- Vue.js 3 with Composition API
- Vite for fast development
- CRUD operations example with Items
- CORS configured for development

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/items` - List all items
- `GET /api/items/{id}` - Get item by ID
- `POST /api/items` - Create new item
- `PUT /api/items/{id}` - Update item
- `DELETE /api/items/{id}` - Delete item

## Database Configuration

The database connection is configured in `backend/app/config.py` and uses environment variables. Copy `.env.example` to `backend/.env` to customize settings.
