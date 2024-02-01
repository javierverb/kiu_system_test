from random import randint
from uuid import uuid4

from entities.company import Company
from entities.shipping import Package, Shipment
from entities.user import User


def random_field_string(field_name: str, posfix: str = "") -> str:
    return f"{field_name}{randint(0, 1000)}{posfix}"


def create_user(company_id) -> User:
    return User(
        company_id=company_id,
        username=random_field_string("username"),
        email=random_field_string("email", "@example.com"),
        password=random_field_string("password"),
        is_active=True,
    )


def create_package(**kwargs) -> Package:
    params = {
        "name": random_field_string("package"),
        "weight": 100.0,
        **kwargs,
    }
    return Package(**params)


def create_shipment(amount_of_packages: int = 1, **kwargs) -> Shipment:
    packages = [create_package() for _ in range(amount_of_packages)]
    params = {
        "origin": random_field_string("origin"),
        "destination": random_field_string("destination"),
        "packages": packages,
        **kwargs,
    }
    return Shipment(**params)


def create_company(
    company_name=random_field_string("company"),
    amount_of_shipments: int = 1,
    amount_of_packages: int = 1,
) -> Company:
    company_name = company_name
    shipments = [create_shipment(amount_of_packages=amount_of_packages) for _ in range(amount_of_shipments)]
    return Company(name=company_name, shipments=shipments)
