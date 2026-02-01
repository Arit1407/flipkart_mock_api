from pydantic import BaseModel, Field
from typing import Optional

class Order(BaseModel):
    OrderID: int

    OrderDate: str
    OrderTime: str
    DeliveryDate: str
    DeliveryTime: str

    ReturnDate: Optional[str]
    ReturnTime: Optional[str]
    ReturnReason: Optional[str]

    Product_Name: str
    Category: str
    Company: str

    ProductPrice: Optional[float]
    Quantity: Optional[int]

    PaymentMethod: Optional[str]

    CustomerAge: Optional[int]
    CustomerGender: Optional[str]

    City: Optional[str]
    State: Optional[str]

    CustomerPurchaseHistory: Optional[int]
    CustomerReturnHistory: Optional[int]

    ProductRating: Optional[float]
    Product_Warranty: Optional[str]

    ShippingMode: Optional[str]
    DiscountApplied: Optional[float]

    Return_Risk: Optional[int]
