import pytest

from src.utils import Category, Product


@pytest.fixture
def correct_init_category():
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром,"
                    , [1, 2, 3, 4])


def test_init_category(correct_init_category):
    assert correct_init_category.name == 'Телевизоры'
    assert correct_init_category.description == "Современный телевизор, который позволяет наслаждаться просмотром,"
    " станет вашим другом и помощником"
    assert correct_init_category.products == [1, 2, 3, 4]


@pytest.fixture
def correct_init_products():
    return Product("Iphone 15", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(correct_init_products):
    assert correct_init_products.name == "Iphone 15"
    assert correct_init_products.description == "256GB, Серый цвет, 200MP камера"
    assert correct_init_products.price == 180000.0
    assert correct_init_products.quantity == 5
