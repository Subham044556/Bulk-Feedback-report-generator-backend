# main.py

from fastapi import FastAPI
from middleware import setup_cors
from routes import router as api_router

# Create the main FastAPI application instance
app = FastAPI(title="Bulk Feedback Report Generator API")

# Configure CORS middleware by calling the function from middleware.py
setup_cors(app)

# Include the API router from routes.py
# All routes defined in routes.py will now be part of the main app
app.include_router(api_router)

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the Bulk Feedback Report Generator API!"}