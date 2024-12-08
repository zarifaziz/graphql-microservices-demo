from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class Product:
    """
    Product model representing items in the catalog.
    
    Parameters
    ----------
    id : int
        Unique identifier for the product
    name : str
        Name of the product
    description : str
        Detailed description of the product
    price : Decimal
        Price of the product
    stock : int
        Current stock quantity
    category : str
        Product category
    """
    id: int
    name: str
    description: str
    price: Decimal
    stock: int
    category: str 