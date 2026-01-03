from pydantic import BaseModel
from typing import Optional, List


class Comment(BaseModel):
    content: str
    replies: Optional[List["Comment"]] = None  # Self-referencing field


Comment.model_rebuild()  # Required to resolve forward references

# Example usage

if __name__ == "__main__":
    comment1 = Comment(content="This is the first comment.")
    comment2 = Comment(content="This is a reply to the first comment.", replies=[comment1])
    comment3 = Comment(content="This is another top-level comment.", replies=[comment2])

    print(comment3)