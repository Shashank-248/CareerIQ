# CareerIQ Prototype (H2S-HTN)

This repo contains a minimal FastAPI backend prototype and supporting docs/assets for the CareerIQ experience.

- Backend: see `backend/` (FastAPI app, in-memory state)
- Design inspo: `static files/`
- Docs: `documents/`

## Quick Start (Windows PowerShell)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Open API docs at: http://localhost:8000/docs

## Environment
- Copy `backend/.env.example` to `backend/.env` and adjust as needed.
- The backend reads env via `pydantic-settings` / `python-dotenv`.

```env
APP_NAME=CareerIQ Backend
ENVIRONMENT=dev
ENCRYPTION_KEY=change-me
MODEL_SERVER_PRIMARY=http://127.0.0.1:11434
MODEL_SERVER_SECONDARY=http://127.0.0.1:11434
```

## What’s Implemented
Back-end capabilities implemented now (see `backend/README.md` for details):
- Device registration, profile CRUD, skills upsert/list
- Chat pipeline stub with language detection and model routing heuristic
- Opportunities + daily challenges (mock data)
- Resume parsing (plain-text + naive skill inference)
- Gamification status and points/badges logic

## What’s Next
- Wire real LLM calls (Ollama HTTP) in `routes_chat.py`
- Build a minimal frontend to exercise flows end-to-end
- Add persistence strategy (still favor client-side; keep server stateless)
- Rate limiting and better input validation

## Repo Hygiene
- Git ignores virtual envs, caches, and `.env` files.
- Do not commit your virtual environment or secrets.

## Contributing
- Use feature branches; open PRs for review.
- Keep changes scoped and documented.
