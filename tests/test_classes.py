import pytest
from src.classes import Product, Category


@pytest.fixture
def product_value():
    return Product("Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_product(product_value):
    assert product_value.name == "Samsung S23 Ultra"
    assert product_value.description == "256GB, Серый цвет, 200MP камера"
    assert product_value.price == 180000.0
    assert product_value.quantity == 5


@pytest.fixture
def category_value():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    [])


def test_category(category_value):
    assert category_value.name == "Смартфоны"

    assert category_value.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert category_value.products == []