import pytest
from src.product import Product


@pytest.fixture
def correct_init_products():
    return Product("Iphone 15", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(correct_init_products):
    assert correct_init_products.name == "Iphone 15"
    assert correct_init_products.description == "256GB, Серый цвет, 200MP камера"
    assert correct_init_products.price == 180000.0
    assert correct_init_products.quantity == 5
