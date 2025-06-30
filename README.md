# SkyProProject: Управление товарами и категориями

Проект для управления каталогом товаров с системой категоризации. Реализованы базовые классы для работы с продуктами и категориями.

## 🛠 Технологии
- Python 3.8+
- Poetry (управление зависимостями)
- Git (контроль версий)
- PyCharm (рекомендуемая IDE)

## 📦 Структура проекта
SkyProProject/
├── src/
│ ├── classes.py # Основные классы Product и Category
│ └── main.py # Точка входа (пример использования)
├── tests/
│ └── test_classes.py # Юнит-тесты
├── pyproject.toml # Конфигурация Poetry
└── README.md # Документация

## 🧩 Основные классы

### `Product`
```python
class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0  # Счётчик всех товаров
    
    def __init__(self, name, description, price, quantity):
        ...

class Category:
    name: str
    description: str
    products: list
    category_count = 0  # Счётчик всех категорий
    
    def __init__(self, name, description, products):
        ...