# API Documentation

FastAPI automatically generates:
- Swagger UI
- OpenAPI schema

Available at:
- `/docs`
- `/redoc`

## API Design

### Base path
`/api/v1`

### Route groups
- `/auth`
- `/users`
- `/portfolios`
- `/holdings`
- `/transactions`
- `/dashboard`
- `/market`
- `/insights`
- `/watchlists`
- `/health`

### Authentication
- `POST /api/v1/auth/signup` — create account
- `POST /api/v1/auth/login` — obtain JWT token
- `POST /api/v1/auth/refresh` — refresh access token
- `POST /api/v1/auth/logout` — revoke session or token

### Health Endpoint
- `GET /api/v1/health` — data health endpoint

Response example:
```json
{
  "status": "healthy"
}
```

### Portfolio
- `GET /api/v1/portfolios` — list user portfolios
- `POST /api/v1/portfolios` — create portfolio
- `GET /api/v1/portfolios/{id}` — portfolio details
- `PUT /api/v1/portfolios/{id}` — update portfolio
- `DELETE /api/v1/portfolios/{id}` — delete portfolio

### Holdings
- `GET /api/v1/portfolios/{id}/holdings` — list holdings
- `POST /api/v1/portfolios/{id}/holdings` — add holding
- `PUT /api/v1/holdings/{id}` — update holding
- `DELETE /api/v1/holdings/{id}` — remove holding
- `POST /api/v1/holdings/import` — import holdings

### Dashboard
- `GET /api/v1/dashboard/summary`
- `GET /api/v1/dashboard/allocation`
- `GET /api/v1/dashboard/performance`
- `GET /api/v1/dashboard/watchlist`

### Transactions
- `GET /api/v1/transactions`
- `POST /api/v1/transactions`
- `GET /api/v1/transactions/{id}`

### Market
- `GET /api/v1/market/indices`
- `GET /api/v1/market/trending`
- `GET /api/v1/market/news`
- `GET /api/v1/market/stocks/{symbol}`

### Insights
- `GET /api/v1/insights/recommendations`
- `GET /api/v1/insights/risk-analysis`
- `GET /api/v1/insights/sentiment`

## Backend app structure
```text
app/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── services/
├── repositories/
├── workers/
└── utils/
```