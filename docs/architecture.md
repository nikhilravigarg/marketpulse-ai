# System Architecture

This document describes the high-level architecture of MarketPulse AI, including application layers, system responsibilities, data flow, and future scalability considerations.

## Monorepo Structure

### `frontend/`
Next.js frontend application responsible for:
- authentication UI
- portfolio dashboards
- charts and analytics
- user interaction

### `backend/`
FastAPI backend responsible for:
- REST APIs
- authentication and authorization
- portfolio management
- business logic
- market data processing

### `database/`
Contains:
- SQL schema definitions
- ER diagrams
- migration planning
- seed scripts

### `docs/`
Project documentation including:
- PRD
- architecture diagrams
- API contracts
- UI/UX wireframes

### `docker/`
Dockerfiles and `docker-compose` configuration for local development and deployment.

### `.github/`
CI/CD workflows, GitHub Actions, and automation pipelines.

## Architecture Principles

- API-first backend design
- Clear separation of concerns
- Scalable service-oriented structure
- Async-ready backend processing
- Database normalization
- Modular frontend components
- Production-style folder organization

## High-Level Request Flow

1. User accesses the Next.js frontend application
2. Frontend communicates with FastAPI APIs over HTTP/REST
3. Backend validates authentication and processes business logic
4. Backend interacts with PostgreSQL for portfolio and user data persistence
5. Backend returns structured JSON responses
6. Frontend renders dashboards, analytics, and portfolio insights

## Planned Future Enhancements

The architecture is intentionally designed to evolve incrementally.

Future components may include:
- Redis caching layer
- Celery background workers
- Market data ingestion pipelines
- AI recommendation engine
- News sentiment analysis
- Real-time websocket updates
- Event-driven processing
- Dockerized deployment environments

## Proposed System Components

### Frontend
- Next.js
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

### Infrastructure
- Docker
- GitHub Actions
- Vercel/Render deployment

## Deployment diagram

```text
User
 ↓
Next.js Frontend
 ↓
FastAPI Backend
 ↓
PostgreSQL
```

## Backend app structure

```text
backend/app/
├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
├── workers/
└── utils/
```
