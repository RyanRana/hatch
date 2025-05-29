# Hatch – AI Job Discovery Tool

Hatch is an AI-powered job discovery platform. Just upload your resume and enter a job title — Hatch will fetch job listings and rank them using semantic similarity.

## 🧠 Tech Stack

- Frontend: React + Tailwind
- Backend: FastAPI + Sentence Transformers
- Matching: Cosine Similarity on Embeddings
- Deployment: Docker + Render or Vercel

## 🛠️ Local Setup

```bash
git clone https://github.com/youruser/hatch.git
cd hatch
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/match

## 🚀 Deployment Options

### Option 1: Render (All-in-One)

- Deploy `/backend` as a Web Service (Python)
- Deploy `/frontend` as a Web Service (Node.js)

### Option 2: Fly.io + Vercel

- Fly.io for `/backend` with Dockerfile
- Vercel for `/frontend` with environment var:
  ```env
  REACT_APP_API_URL=https://<your-backend>.fly.dev
  ```

