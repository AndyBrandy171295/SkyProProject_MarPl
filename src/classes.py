class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        if existing_products is None:
            existing_products = []

        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        for product in existing_products:
            if (
                product.name.lower() == name.lower()
            ):  # Исправлено existing_products.name на product.name
                product.quantity += quantity
                product.price = max(product.price, price)
                print(
                    f"Товар {name} уже существует. Объединили количество и выбрали большую цену"
                )
                return product

        return cls(name, description, price, quantity)


class Category:
    name: str
    description: str
    __products: list
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1

    @property
    def products(self):
        products_string = ""
        for product in self.__products:  # Исправлено: итерация по self.__products
            products_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_string

    def add_product(self, product):  # Исправлено: параметр products → product
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)

    @property
    def product_count(self):
        return len(self.__products)


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
