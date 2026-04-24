from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.analyzer import analyze_resume_workflow

router = APIRouter()


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
  if not file.filename.endswith(".pdf"):
    raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

  try:
    content = await file.read()
    result = await analyze_resume_workflow(content, job_description)
    return result
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
