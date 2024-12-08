from fastapi import FastAPI, HTTPException
from typing import List
from decimal import Decimal

from .models import Product

app = FastAPI()

# Simulated database
products_db = [
    Product(
        id=1,
        name="Laptop Pro",
        description="High-performance laptop for professionals",
        price=Decimal("1299.99"),
        stock=50,
        category="Electronics"
    ),
    Product(
        id=2,
        name="Wireless Mouse",
        description="Ergonomic wireless mouse",
        price=Decimal("29.99"),
        stock=100,
        category="Accessories"
    )
]

@app.get("/products/", response_model=List[Product])
async def get_products():
    """Get all products"""
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Get a specific product by ID"""
    product = next((p for p in products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str):
    """Get all products in a specific category"""
    products = [p for p in products_db if p.category.lower() == category.lower()]
    return products 