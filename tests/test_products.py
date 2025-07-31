from src.products import Smartphone, LawnGrass
import pytest


@pytest.fixture
def product_value_phone():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def product_value_lg():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


def test_smartphone(product_value_phone):
    assert product_value_phone.efficiency == 98.2
    assert product_value_phone.model == "15"
    assert product_value_phone.memory == 512
    assert product_value_phone.color == "Gray space"


def test_lawn_grass(product_value_lg):
    assert product_value_lg.country == "США"
    assert product_value_lg.germination_period == "5 дней"
    assert product_value_lg.color == "Темно-зеленый"


def test_add_product():
    phone1 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    phone2 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )
    lg1 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    lg2 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert phone1 + phone2 == 2114000
    assert lg2 + lg1 == 16750

    with pytest.raises(TypeError, match="Нельзя складывать продукты разных типов!"):
        phone1 + lg1
