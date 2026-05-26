# MarketPulse AI

MarketPulse AI is a single-monorepo project for a portfolio-first investing dashboard. Start simple, build MVP features first, then expand into market insights and AI recommendations.

## Vision
MarketPulse AI aims to help retail investors make informed decisions through portfolio analytics, market intelligence, and AI-assisted insights.

The platform will evolve from a portfolio management dashboard into a real-time investment intelligence system capable of:
- portfolio tracking
- risk analysis
- market monitoring
- news sentiment analysis
- AI-generated investment insights

## Tech Stack
- Frontend: Next.js, TypeScript, Tailwind CSS, App Router
- Backend: FastAPI, Python, SQLAlchemy
- Database: PostgreSQL-compatible (Supabase / Neon recommended)
- Deployment: Docker, `docker-compose`

## Repo Structure
- `frontend/` — Next.js user interface
- `backend/` — FastAPI REST APIs
  - `app/`
    - `api/`
    - `core/`
    - `db/`
    - `models/`
    - `repositories/`
    - `schemas/`
    - `services/`
    - `workers/`
    - `utils/`
- `database/` — SQL schema, ER diagrams, database design
- `docs/` — PRD, architecture notes, API design, wireframes
- `docker/` — Docker and deployment config
- `.github/` — CI/CD workflows

## Architecture
The current architecture is intentionally simple:
- Frontend talks to backend
- Backend persists portfolio data to PostgreSQL
- Documentation and ER design are stored in `/docs`

See `docs/architecture.md` and `docs/er-diagram.md` for the full architecture and database design.

## Setup
### 1. Frontend
```bash
cd frontend
npx create-next-app@latest . \
  --typescript --eslint --tailwind --src-dir --app
```

### 2. Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic
pip freeze > requirements.txt
```

### 3. Database
Use Supabase or Neon for PostgreSQL if you do not want to run Postgres locally.

### 4. Run locally
```bash
cd backend
uvicorn app.main:app --reload
```

## Screenshots
Screenshots and UI previews will be added here once the frontend is built.

## Roadmap
- ✅ Day 1: monorepo structure, docs, README
- ✅ Day 2: initialize frontend and backend
- Next: auth, portfolio CRUD, holdings management
- Next: dashboard summary, performance metrics
- Future: AI market insights, recommendations, watchlists

## Notes
Focus on the first MVP: signup/login, portfolio creation, add holdings, dashboard view.
