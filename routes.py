# routes.py

import os
import shutil
import time
from typing import List, Optional

from fastapi import APIRouter, File, UploadFile, Form

# APIRouter allows us to define routes in a separate file
router = APIRouter()

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload/")
async def upload_data(
    student_files: List[UploadFile] = File(...),
    assignment_brief: UploadFile = File(...),
    assignment_type: str = Form(...),
    grading_intensity: str = Form(...),
    custom_categories: Optional[str] = Form(None),
    additional_notes: Optional[str] = Form(None),
    output_format: str = Form(...)
):
    """
    Handles the file uploads and form data submission.
    """
    # --- 1. Save Files ---
    for file in student_files:
        with open(os.path.join(UPLOAD_DIR, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    with open(os.path.join(UPLOAD_DIR, assignment_brief.filename), "wb") as buffer:
        shutil.copyfileobj(assignment_brief.file, buffer)

    # --- 2. Process Data (Simulation) ---
    print(f"Processing request for assignment type: {assignment_type}")
    print(grading_intensity)
    print(custom_categories)
    print(additional_notes)
    print(output_format)
    time.sleep(2)  # Simulate work being done

    # --- 3. Return Structured Response ---
    mock_summary_data = [
        {
            "name": "Riya Sharma",
            "roll": "23CS1023",
            "type": assignment_type,
            "summary": "Great ideas, moderate grammar mistakes.",
            "strengths": "Ideas, Creativity",
            "improvements": "Grammar, clarity",
        },
        {
            "name": "Amit Kumar",
            "roll": "23ME1045",
            "type": assignment_type,
            "summary": "Excellent structure and well-researched.",
            "strengths": "Structure, Research",
            "improvements": "Add more examples",
        },
    ]

    return {"message": "Files processed successfully", "summary": mock_summary_data}