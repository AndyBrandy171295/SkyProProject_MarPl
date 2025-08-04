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
        if self.quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен!')
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

    def middle_price(self):
        try:
            total_price = 0
            count_product = 0
            for product in self._products:
                count_product += 1
                total_price += product.price
            total_middle_price = round(total_price / count_product, 2)
            return total_middle_price
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
