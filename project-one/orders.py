from fastapi import APIRouter
from models.order import Order

router = APIRouter(prefix="/orders", tags=["orders"])

fake_db = []

@router.post("/")
def create_order(order: Order):
    fake_db.append(order)
    return {"message": "Order created", "order": order}

@router.get("/")
def list_orders():
    return fake_db