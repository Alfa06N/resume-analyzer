from app.utils.pdf_parser import extract_text_from_pdf
from google import genai
import json
import os
from dotenv import load_dotenv
from fastapi import File, UploadFile, Form

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


async def analyze_resume_workflow(pdf_file: UploadFile = File(...), job_description: str = Form(...)) -> dict:
  if "DEMO" in job_description.upper():
    return {
        "score": 92,
        "match_summary": "DEMO: Your profile shows a strong match for the Software Engineer role, with relevant experience in Python, Java, and cloud technologies. To further improve your chances, consider adding more specific achievements and quantifiable results to your resume.",
        "keyword_gaps": ["Kubernetes", "AWS Lambda", "Redis"],
        "suggestions": [
            "Include specific achievements with quantifiable results (e.g., 'Improved application performance by 30% through code optimization').",
            "Highlight any experience with Kubernetes, AWS Lambda, and Redis, as these are key technologies mentioned in the job description.",
            "Consider adding a summary section at the top of your resume that clearly states your career goals and key qualifications."
        ]
    }
  resume_text = extract_text_from_pdf(pdf_file)

  prompt = f"""
    You are an expert ATS (Applicant Tracking System) analyzer.
    Compare the Resume Text against the Job Description.
    
    Resume: {resume_text}
    Job Description: {job_description}
    
    Return ONLY a JSON object with this exact structure:
    {{
      "score": (0-100 integer),
      "keyword_gaps": ["list", "of", "missing", "keywords"],
      "suggestions": ["specific", "improvement", "tips"],
      "match_summary": "short explanation"
    }}
    """

  response = client.models.generate_content(
      model="models/gemini-2.5-flash", contents=prompt)
  clean_json = response.text.strip().replace('```json', '').replace('```', '')

  return json.loads(clean_json)
