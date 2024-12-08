import strawberry
from typing import List
from dataclasses import dataclass

@strawberry.type
class User:
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool

@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> List[User]:
        # Implementation will be added later
        pass

    @strawberry.field
    async def user(self, id: int) -> User:
        # Implementation will be added later
        pass

schema = strawberry.Schema(query=Query) 