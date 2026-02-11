import random
from datetime import datetime

from faker import Faker
from pydantic import BaseModel, EmailStr, Field, field_validator

fake = Faker()

ALLOWED_COUNTRIES = [
    "India",
    "United States",
    "Canada",
    "Australia",
    "Israel",
    "New Zealand",
    "Singapore",
]


class User(BaseModel):
    name: str = Field(default_factory=fake.name)
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=lambda: fake.password(length=12))
    title: str = "Mr"

    birth_date: int = Field(default_factory=lambda: int(fake.day_of_month()))
    birth_month: int = Field(default_factory=lambda: int(fake.month()))
    birth_year: int = Field(default_factory=lambda: int(fake.year()))

    firstname: str = Field(default_factory=fake.first_name)
    lastname: str = Field(default_factory=fake.last_name)
    company: str = Field(default_factory=fake.company)
    address1: str = Field(default_factory=fake.street_address)
    address2: str | None = None
    country: str = Field(default_factory=lambda: random.choice(ALLOWED_COUNTRIES))
    zipcode: str = Field(default_factory=fake.zipcode)
    state: str = Field(default_factory=fake.state)
    city: str = Field(default_factory=fake.city)
    mobile_number: str = Field(default_factory=fake.phone_number)

    @field_validator("birth_year")
    @classmethod
    def check_birth_year(cls, v: int):
        current_year = datetime.now().year
        if v < 1900 or v > current_year:
            raise ValueError(f"Birth year must be between 1900 and {current_year}")
        return v
