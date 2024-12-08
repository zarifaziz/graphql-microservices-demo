import strawberry
from typing import List
from decimal import Decimal
import httpx
from dataclasses import dataclass
import os

@strawberry.type
class User:
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool

@strawberry.type
class Product:
    id: int
    name: str
    description: str
    price: Decimal
    stock: int
    category: str

@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> List[User]:
        """Fetch all users from the users service"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{os.getenv('USERS_SERVICE_URL')}/users/")
            response.raise_for_status()
            return [User(**user) for user in response.json()]

    @strawberry.field
    async def user(self, id: int) -> User:
        """Fetch a specific user by ID"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{os.getenv('USERS_SERVICE_URL')}/users/{id}")
            if response.status_code == 404:
                raise ValueError(f"User with ID {id} not found")
            response.raise_for_status()
            return User(**response.json())

    @strawberry.field
    async def products(self) -> List[Product]:
        """Fetch all products from the products service"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{os.getenv('PRODUCTS_SERVICE_URL')}/products/")
            response.raise_for_status()
            return [Product(**product) for product in response.json()]

    @strawberry.field
    async def product(self, id: int) -> Product:
        """Fetch a specific product by ID"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{os.getenv('PRODUCTS_SERVICE_URL')}/products/{id}")
            if response.status_code == 404:
                raise ValueError(f"Product with ID {id} not found")
            response.raise_for_status()
            return Product(**response.json())

    @strawberry.field
    async def products_by_category(self, category: str) -> List[Product]:
        """Fetch all products in a specific category"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{os.getenv('PRODUCTS_SERVICE_URL')}/products/category/{category}"
            )
            response.raise_for_status()
            return [Product(**product) for product in response.json()]

schema = strawberry.Schema(query=Query) 