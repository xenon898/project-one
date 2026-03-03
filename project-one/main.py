from fastapi import FastAPI
from routers import orders

app = FastAPI(
    title="Orders Service",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "healthy"}

app.include_router(orders.router)