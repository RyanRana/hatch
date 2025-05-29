from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer, util
from typing import List
from PyPDF2 import PdfReader
import uvicorn, os, json

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text(file: UploadFile):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        return file.file.read().decode('utf-8')

@app.post("/match")
async def match_jobs(
    resume_file: UploadFile = File(...),
    search_term: str = Form(...)
):
    resume_text = extract_text(resume_file)

    with open("jobs.json") as f:
        jobs = json.load(f)

    job_texts = [f"{job['title']} {job['description']}" for job in jobs]
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    job_embs = model.encode(job_texts, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(resume_emb, job_embs)[0]
    scored_jobs = sorted(zip(jobs, scores), key=lambda x: x[1], reverse=True)[:10]

    return [{"job": job, "score": float(score)} for job, score in scored_jobs]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
