# Portfolio Resume AI

A full-stack AI-powered resume analyzer that helps you tailor your resume to any job description. Upload your resume as a PDF, paste a job posting, and get an instant ATS compatibility score along with actionable feedback — all powered by Google Gemini.

---

## Features

- **ATS Score** — Get a 0–100 match score showing how well your resume aligns with the job description
- **Keyword Gap Analysis** — See exactly which keywords are missing from your resume
- **AI Suggestions** — Receive specific, actionable tips to improve your chances
- **PDF Upload** — Drag and drop or browse to upload your resume
- **Dark Mode** — Full theme support
- **Demo Mode** — Try it out without uploading anything by typing `DEMO` in the job description

---

## Tech Stack

### Frontend

- [Vue 3](https://vuejs.org/) + TypeScript
- [Vite](https://vitejs.dev/)
- [Tailwind CSS v4](https://tailwindcss.com/)
- [shadcn-vue](https://www.shadcn-vue.com/) (via reka-ui)
- [Pinia](https://pinia.vuejs.org/) for state management
- [VueUse](https://vueuse.org/) for color mode handling

### Backend

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini 2.5 Flash](https://ai.google.dev/) for AI analysis
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF text extraction
- [Uvicorn](https://www.uvicorn.org/) ASGI server

---

## Getting Started

### Prerequisites

- Node.js 18+ and [pnpm](https://pnpm.io/)
- Python 3.10+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

---

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Start the server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

---

### Frontend Setup

```bash
cd frontend
pnpm install
pnpm dev
```

The app will be available at `http://localhost:5173`.

---

## API

### `POST /api/analyze`

Analyzes a resume against a job description.

| Field             | Type   | Description                           |
| ----------------- | ------ | ------------------------------------- |
| `file`            | File   | Resume in PDF format                  |
| `job_description` | string | The job posting text to match against |

**Response:**

```json
{
  "score": 85,
  "match_summary": "Strong match with relevant experience in...",
  "keyword_gaps": ["Kubernetes", "Redis"],
  "suggestions": [
    "Add quantifiable achievements to your experience section.",
    "Mention your experience with Kubernetes in the skills section."
  ]
}
```

---

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/routes/     # FastAPI route handlers
│   │   ├── services/       # Gemini AI analysis logic
│   │   ├── utils/          # PDF parsing utilities
│   │   └── main.py         # App entry point & CORS config
│   └── requirements.txt
│
└── frontend/
    └── src/
        ├── api/            # Axios API client
        ├── components/     # Vue components & shadcn-vue UI
        ├── stores/         # Pinia state management
        └── App.vue
```

---

## License

MIT
