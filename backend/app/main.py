from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Create the FastAPI application instance.
app = FastAPI(
    title="MarketPulse API",
    description="A lightweight FastAPI demo for portfolio and holdings management.",
    version="0.1.0",
)

# --- Models ---
# Pydantic models define the request and response shapes for FastAPI.

class User(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None


class PortfolioCreate(BaseModel):
    name: str = Field(..., example="Retirement Portfolio")
    description: Optional[str] = Field(None, example="Long-term diversified holdings")


class Portfolio(PortfolioCreate):
    id: int
    user_id: int


class HoldingCreate(BaseModel):
    symbol: str = Field(..., example="AAPL")
    name: Optional[str] = Field(None, example="Apple Inc.")
    quantity: float = Field(..., example=10.5)
    average_price: float = Field(..., example=150.0)


class Holding(HoldingCreate):
    id: int
    portfolio_id: int


class DashboardSummary(BaseModel):
    total_portfolios: int
    total_holdings: int
    total_value_usd: float


# --- In-memory demo storage ---
# This is only used for examples and should be replaced by a database in production.
users = [
    User(id=1, email="alice@example.com", full_name="Alice Smith"),
    User(id=2, email="bob@example.com", full_name="Bob Johnson"),
]

portfolios = [
    Portfolio(id=1, user_id=1, name="Retirement Portfolio", description="Long-term holdings"),
    Portfolio(id=2, user_id=1, name="Growth Portfolio", description="High-growth stocks"),
]

holdings = [
    Holding(id=1, portfolio_id=1, symbol="AAPL", name="Apple Inc.", quantity=20, average_price=130),
    Holding(id=2, portfolio_id=1, symbol="MSFT", name="Microsoft Corp.", quantity=15, average_price=210),
]

next_portfolio_id = 3
next_holding_id = 3


# --- Endpoints ---

@app.get("/api/v1/health")
def health():
    """Health check endpoint.

    Returns a simple status message so you can verify the service is running.
    """
    return {"status": "healthy"}


@app.get("/api/v1/users", response_model=List[User])
def list_users():
    """Return a list of users."""
    return users


@app.get("/api/v1/portfolios", response_model=List[Portfolio])
def list_portfolios(user_id: Optional[int] = None):
    """Return portfolios, optionally filtered by user ID.

    Query parameters:
    - user_id: optional filter to return portfolios owned by a specific user.
    """
    if user_id is not None:
        return [p for p in portfolios if p.user_id == user_id]
    return portfolios


@app.post("/api/v1/portfolios", response_model=Portfolio, status_code=201)
def create_portfolio(payload: PortfolioCreate, user_id: int = 1):
    """Create a new portfolio for the default example user.

    In a real app, user_id would come from authentication.
    """
    global next_portfolio_id
    portfolio = Portfolio(id=next_portfolio_id, user_id=user_id, **payload.dict())
    portfolios.append(portfolio)
    next_portfolio_id += 1
    return portfolio


@app.put("/api/v1/portfolios/{portfolio_id}", response_model=Portfolio)
def update_portfolio(portfolio_id: int, payload: PortfolioCreate):
    """Update an existing portfolio by ID."""
    for portfolio in portfolios:
        if portfolio.id == portfolio_id:
            portfolio.name = payload.name
            portfolio.description = payload.description
            return portfolio
    raise HTTPException(status_code=404, detail="Portfolio not found")


@app.delete("/api/v1/portfolios/{portfolio_id}", status_code=204)
def delete_portfolio(portfolio_id: int):
    """Delete a portfolio and its holdings."""
    global portfolios, holdings
    portfolios = [p for p in portfolios if p.id != portfolio_id]
    holdings = [h for h in holdings if h.portfolio_id != portfolio_id]
    return None


@app.get("/api/v1/portfolios/{portfolio_id}/holdings", response_model=List[Holding])
def list_holdings(portfolio_id: int):
    """Return all holdings for a portfolio."""
    return [h for h in holdings if h.portfolio_id == portfolio_id]


@app.post("/api/v1/portfolios/{portfolio_id}/holdings", response_model=Holding, status_code=201)
def add_holding(portfolio_id: int, payload: HoldingCreate):
    """Add a new holding to a portfolio."""
    global next_holding_id
    if not any(p.id == portfolio_id for p in portfolios):
        raise HTTPException(status_code=404, detail="Portfolio not found")

    holding = Holding(id=next_holding_id, portfolio_id=portfolio_id, **payload.dict())
    holdings.append(holding)
    next_holding_id += 1
    return holding


@app.get("/api/v1/dashboard/summary", response_model=DashboardSummary)
def dashboard_summary():
    """Return a simple dashboard summary for the current portfolio data."""
    total_value = sum(h.quantity * h.average_price for h in holdings)
    return DashboardSummary(
        total_portfolios=len(portfolios),
        total_holdings=len(holdings),
        total_value_usd=total_value,
    )
