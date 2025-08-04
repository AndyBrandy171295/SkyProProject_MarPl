# Каталог товаров SkyProProject
https://img.shields.io/badge/Python-3.8+-blue?logo=python
https://img.shields.io/badge/Poetry-1.2+-orange?logo=poetry
https://img.shields.io/badge/Git-enabled-green?logo=git

Проект для управления каталогом товаров с системой категоризации. Реализованы базовые классы для работы с продуктами и категориями, а также специализированные классы для смартфонов и газонной травы.

## 🛠 Технологии
Python 3.8+

Poetry (управление зависимостями)

Git (контроль версий)

Pytest (тестирование)

SkyProProject/
├── src/
│   ├── __init__.py
│   ├── classes.py       # Основные классы Product и Category
│   ├── products.py      # Специализированные классы Smartphone и LawnGrass
│   └── main.py          # Точка входа (пример использования)
├── tests/
│   ├── __init__.py
│   ├── test_classes.py  # Тесты для базовых классов
│   └── test_products.py # Тесты для специализированных классов
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md

## 🧩 Основные классы
* Product - Базовый класс продукта

class Product:
    def __init__(self, name, description, price, quantity):
        # Инициализация продукта
        pass
    
    @property
    def price(self):
        # Возвращает цену продукта
        pass
    
    @price.setter
    def price(self, new_price):
        # Устанавливает новую цену с валидацией
        pass
    
    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        # Фабричный метод для создания/обновления продукта
        pass
    
    def __add__(self, other):
        # Сложение продуктов по стоимости
        pass
    
    def __str__(self):
        # Строковое представление продукта
        pass
* Category - Класс категории товаров

class Category:
    def __init__(self, name, description, products):
        # Инициализация категории
        pass
    
    @property
    def products(self):
        # Возвращает строковое представление всех продуктов
        pass
    
    def add_product(self, product):
        # Добавляет продукт в категорию
        pass
    
    @property
    def product_count(self):
        # Возвращает количество продуктов в категории
        pass
    
    def __str__(self):
        # Строковое представление категории
        pass
## Специализированные классы

* Smartphone - Класс для смартфонов

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        # Инициализация смартфона
        pass
    
    def __add__(self, other):
        # Сложение только смартфонов
        pass

* LawnGrass - Класс для газонной травы

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        # Инициализация газонной травы
        pass
    
    def __add__(self, other):
        # Сложение только газонной травы
        pass

## Дополнительные компоненты

* PrintMixin - Миксин для логирования

class PrintMixin:
    def __init__(self):
        """Автоматический вывод информации при создании объекта"""
        print(repr(self))

    def __repr__(self):
        """Универсальное строковое представление объекта"""
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'

* BaseProduct - Абстрактный базовый класс

class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(self):
        """Абстрактный метод создания продукта"""
        pass

## 🚀 Быстрый старт

* Клонируйте репозиторий:

git clone https://github.com/AndyBrandy171295/SkyProProject.git
cd SkyProProject

* Установите зависимости:

poetry install

* Запустите пример:

poetry run python src/main.py
🧪 Тестирование

poetry run pytest tests/ -v
📊 Пример работы

## Создание смартфона
iphone = Smartphone("iPhone 15", "512GB, Space Gray", 99990.0, 10,
                    98.2, "15", 512, "Gray")

## Создание газонной травы
grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20,
                  "Россия", "7 дней", "Зеленый")

## Создание категории
electronics = Category("Электроника", "Техника для дома", [iphone])
gardening = Category("Сад", "Товары для сада", [grass])

print(iphone)
print(grass)
print(electronics)
print(gardening)

🤝 Как внести вклад
Форкните репозиторий

Создайте ветку (git checkout -b feature/your-feature)

Сделайте коммит (git commit -m 'Add some feature')

Запушите изменения (git push origin feature/your-feature)

Откройте Pull Request

📄 Лицензия
MIT License. Подробнее см. в файле LICENSE.

