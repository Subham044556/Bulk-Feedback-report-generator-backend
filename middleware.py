# middleware.py

from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """
    Configures CORS (Cross-Origin Resource Sharing) middleware for the application.
    This allows the frontend (e.g., http://localhost:3000) to communicate with the backend.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins for simplicity
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods
        allow_headers=["*"],  # Allows all headers
    )
    