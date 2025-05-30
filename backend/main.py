
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
from scraper import scrape_jobs
from ranker import compute_match

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    resume_text = extract_text_from_pdf(contents)
    return {"resume_text": resume_text}

@app.get("/search-jobs")
def search_jobs(q: str):
    return {"links": scrape_jobs(q)}

@app.post("/rank-jobs")
async def rank_jobs(file: UploadFile = File(...), q: str = ""):
    contents = await file.read()
    resume_text = extract_text_from_pdf(contents)
    links = scrape_jobs(q)
    matches = compute_match(resume_text, links)
    sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True)
    return {"ranked": sorted_matches}
