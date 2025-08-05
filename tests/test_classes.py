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


def test_price_setter():
    product = Product("Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 50.0, 5)

    product.price = 75.0
    assert product.price == 75.0


def test_new_product():
    data = {
        "name": "Samsung S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": "200.0",
        "quantity": "3",
    }
    product = Product.new_product(data)
    assert product.name == "Samsung S23 Ultra"
    assert product.price == 200.0

    existing = [Product("Existing", "Desc", 150.0, 5)]
    updated = Product.new_product(
        {
            "name": "Existing",
            "description": "Updated",
            "price": "180.0",
            "quantity": "2",
        },
        existing,
    )
    assert updated.quantity == 7
    assert updated.price == 180.0


@pytest.fixture
def category_value():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )


def test_category_creation():
    products = [
        Product("Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 100.0, 5)
    ]
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products,
    )

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.product_count == 1
    assert Category.category_count > 0


def test_add_product():
    category = Category(
        "Смартфоны", "Смартфоны, как средство не только коммуникации", []
    )
    product = Product("Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 50.0, 3)

    category.add_product(product)
    assert category.product_count == 1


def test_add_product():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 2580000.0


def test_str_product():
    product = Product(
        "Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    result = str(product)
    assert result == "Samsung S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )
    result = str(category)
    assert result == "Смартфоны, количество продуктов: 5 шт."


def test_product_error():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен!"
    ):
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0
        )


def test_category_error():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
