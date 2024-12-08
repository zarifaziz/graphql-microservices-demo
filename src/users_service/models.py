from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool = True 