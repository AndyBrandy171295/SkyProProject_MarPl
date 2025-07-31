from src.print_mixin import PrintMixin
from src.base_product import BaseProduct


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()
        Product.product_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")
        self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        if existing_products is None:
            existing_products = []

        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        for product in existing_products:
            if product.name.lower() == name.lower():
                product.quantity += quantity
                product.price = max(product.price, price)
                print(
                    f"Товар {name} уже существует. Объединили количество и выбрали большую цену"
                )
                return product

        return cls(name, description, price, quantity)

    def __add__(self, other):
        if isinstance(other, Product):
            return (self._price * self.quantity) + (other.price * other.quantity)
        else:
            raise ValueError("Разные типы объектов нельзя суммировать!")

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."


class Category:
    name: str
    description: str
    _products: list
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products if products else []
        Category.category_count += 1

    @property
    def products(self):
        products_string = ""
        for product in self._products:
            products_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_string

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        return self._products.append(product)

    @property
    def product_count(self):
        return len(self._products)

    def __str__(self):
        summ_of_products = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {summ_of_products} шт."


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
