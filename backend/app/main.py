from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(title="Biocommunicator API")

# Include the routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the Biocommunicator API"}