# CareerIQ Backend (Prototype)

Minimal FastAPI backend supporting core prototype flows: device registration, profile, skills, chat (stub with language normalization), opportunities, challenges, resume parsing, gamification status.

## Features Implemented
- Device tier heuristic (`/api/v1/device/register`)
- Profile create + fetch
- Skill upsert/list (0-100 scale with evidence source list)
- Multilingual chat pipeline stub (detect + pseudo translation placeholder)
- Model routing heuristic (local vs primary vs secondary)
- Opportunities mock list
- Daily challenges mock
- Resume parsing endpoint (naive text + keyword skill inference)
- Gamification points/badges evaluation
- Encryption utility (Fernet wrapper) ready for future state persistence

## Tech Stack
- FastAPI, Pydantic v2
- In-memory storage (stateless server) — all persistence will be client-side in final architecture
- Ready to integrate with Ollama model servers (primary/secondary)

## Quick Start (Windows PowerShell)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Open docs: http://localhost:8000/docs

## Key Endpoints
| Purpose | Method | Path |
|---------|--------|------|
| Health | GET | /health |
| API Index | GET | / |
| Device Register | POST | /api/v1/device/register |
| Profile Create | POST | /api/v1/profile/create |
| Profile Get | GET | /api/v1/profile/{user_id} |
| Skills Upsert | POST | /api/v1/skills/upsert |
| Skills List | GET | /api/v1/skills/{user_id} |
| Chat Ask | POST | /api/v1/chat/ask |
| Opportunities | GET | /api/v1/opportunities/list |
| Daily Challenges | GET | /api/v1/challenges/daily |
| Parse Resume | POST | /api/v1/parse/resume?user_id=... (multipart) |
| Gamification Status | GET | /api/v1/gamification/status/{user_id} |

## Example Chat Request
```json
{
  "user_id": "<uuid>",
  "query": "मुझे डेटा साइंस करियर बताओ",
  "language": "hi",
  "device_tier": "budget",
  "allow_local": false
}
```
Response includes model + route annotation.

## Integrating Real LLM (Future Step)
1. Ensure Ollama running on primary server (e.g. gemma3:270m, llama3.2:1b).
2. Create service function calling `POST http://<server>:11434/api/generate`.
3. Swap stub in `routes_chat.py` with real generation, passing normalized English query + minimal context (skills, interests).

## Resume Parsing Future Enhancements
- PDF parsing via `pdfminer.six`
- Optional OCR (pytesseract) for image-based resumes
- Skill scoring weighting by frequency + section (Projects, Experience)

## Gamification Roadmap
- Event hooks: skill_added, challenge_completed, chat_insight_detected
- Rank tiers & progression metrics
- Leaderboard (client-side aggregated JSON to keep server stateless initially)

## Multilingual Roadmap
- Replace placeholder translation with local model or offline translation package
- Add transliteration for code-mixed queries

## Security/Privacy Notes
- Current prototype stores everything in memory on server (volatile). No persistence or user PII.
- Production plan: encryption + client-side persistence only; server ephemeral compute.

## Testing
Run included flow test:
```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m httpx --version  # (optional) ensure httpx present
python tests/test_flow.py
```

## Environment Variables (`.env` supported)
```
APP_NAME=CareerIQ Backend
ENVIRONMENT=dev
ENCRYPTION_KEY=change-me
MODEL_SERVER_PRIMARY=http://192.168.1.100:11434
MODEL_SERVER_SECONDARY=http://192.168.1.101:11434
```

## Next Backend Tasks
- Integrate real LLM call abstraction
- Add context builder (recent skills + top interests)
- Add challenge result submission endpoint to update skill scores adaptively
- Introduce lightweight rate limiting (per user UUID)

## Frontend Coordination
Frontend will:
1. Generate/store UUID
2. Register device
3. Create profile
4. Upload resume for inferred skills
5. Upsert additional skills/projects
6. Use chat with language auto-handled
7. Show opportunities + daily challenges
8. Display gamification status

---
Prototype backend ready for iterative enhancement.
