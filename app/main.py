from fastapi import FastAPI
from app.routes import orders, health

app = FastAPI(
    title="Flipkart Product Returns Mock API",
    description="Mock API serving Flipkart product return data with validation and pagination",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(orders.router)
