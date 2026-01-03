from typing import List,Dict,Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(
    ..., description="The unique identifier for the user")
    name: str = Field(
    ...,min_length=10, max_length=30,
    description="The name of the user")
    courses: List[str] = Field(
        ...,description="List of courses enrolled by the user")
    
user1 = User(
    id=1,
    name="Johnathan Doe",
    courses=["Math", "Science"]
)
