from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.analysis import router as analysis_router

app = FastAPI(title="Resume Analyzer API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(analysis_router, prefix="/api")


@app.get("/")
async def root():
  return {"message": "Resume Analyzer API is running!"}
