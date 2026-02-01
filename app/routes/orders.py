from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from app.data_loader import load_data
from app.models.order import Order
from app.config import MAX_LIMIT

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=List[Order])
def get_orders(
    offset: int = Query(0, ge=0),
    limit: int = Query(10000, ge=1, le=MAX_LIMIT),
    return_risk: Optional[int] = Query(None, ge=0, le=1)
):
    df = load_data()

    if return_risk is not None:
        df = df[df["Return_Risk"] == return_risk]

    if offset >= len(df):
        raise HTTPException(
            status_code=404,
            detail="Offset exceeds dataset size"
        )

    return df.iloc[offset: offset + limit].to_dict(orient="records")


@router.get("/stats")
def dataset_stats():
    df = load_data()
    return {
        "total_rows": len(df),
        "return_rate": round(df["Return_Risk"].mean(), 3),
        "avg_product_price": round(df["ProductPrice"].mean(), 2),
        "avg_discount": round(df["DiscountApplied"].mean(), 2)
    }


@router.get("/target-distribution")
def target_distribution():
    df = load_data()
    return df["Return_Risk"].value_counts(normalize=True).to_dict()
