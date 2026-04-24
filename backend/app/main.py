from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.analysis import router as analysis_router

app = FastAPI(title="Resume Analyzer API")
origins = [
    "http://localhost:5173",
    "https://resume-analyzer-tawny-six.vercel.app",
    "https://resume-analyzer-a52yvsiqy-nicolas-alfaros-projects.vercel.app",
    "https://resume-analyzer-git-main-nicolas-alfaros-projects.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(analysis_router, prefix="/api")


@app.get("/")
async def root():
  return {"message": "Resume Analyzer API is running!"}
