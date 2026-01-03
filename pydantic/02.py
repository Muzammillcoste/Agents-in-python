from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    id: int
    name: str
    courses: list[str]

    @field_validator('name')  
    def name_length(cls, value):
        if not (10 <= len(value) <= 30):
            raise ValueError('Name must be between 10 and 30 characters long')
        return value
    
class employee(BaseModel):
    id: int
    name: str
    department: str
    password: str
    confirm_password: str

    @model_validator(mode='before')
    def check_passwords_match(cls, values):
        if values.get('password') != values.get('confirm_password'):
            raise ValueError('Passwords do not match')
        return values
    
employee1 = employee(id=101, name="Alice Smith", department="HR", password="se", confirm_password="securepass")