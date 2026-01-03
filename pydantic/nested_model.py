from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    name: str
    age: int
    address: Address

# Example usage
if __name__ == "__main__":
    user1 = User(name="John Doe", age=30, address=Address(street="123 Main St", city="Anytown", zip_code="12345"))
    print(user1)