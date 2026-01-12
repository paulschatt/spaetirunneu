from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.database import engine, Base
from .routes import spaetirun

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spaetirun API")

# CORS middleware for Vue.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(spaetirun.SpaetirunRouter.router, prefix="/api/spaetirun", tags=["spaetirun"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Spaetirun API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
