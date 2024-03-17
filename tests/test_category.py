import pytest

from src.category import Category


@pytest.fixture
def correct_init_category():
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром",[1, 2, 3, 4])


def test_init_category(correct_init_category):
    assert correct_init_category.name == 'Телевизоры'
    assert correct_init_category.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert correct_init_category.products == [1, 2, 3, 4]


