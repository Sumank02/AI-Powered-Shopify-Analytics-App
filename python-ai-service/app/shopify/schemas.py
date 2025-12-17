from typing import TypedDict


class SalesRecord(TypedDict):
    product_title: str
    total_quantity: int
    total_sales: float


class InventoryRecord(TypedDict):
    product_title: str
    available_quantity: int
    daily_sales_rate: int
