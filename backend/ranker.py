
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_match(resume_text, job_descriptions):
    resume_embedding = model.encode([resume_text])
    job_embeddings = model.encode(job_descriptions)
    scores = cosine_similarity(resume_embedding, job_embeddings)[0]
    return list(zip(job_descriptions, scores))
