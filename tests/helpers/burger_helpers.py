from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.data.test_data import TEST_BUNS, TEST_INGREDIENTS


def create_test_burger_with_ingredients(bun_data, ingredients_data):
    """Создает бургер с заданными булкой и ингредиентами."""
    from praktikum.burger import Burger
    
    burger = Burger()
    burger.set_buns(Bun(bun_data["name"], bun_data["price"]))
    
    for ingredient_data in ingredients_data:
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        burger.add_ingredient(ingredient)
    
    return burger


def calculate_expected_price(bun_price, ingredients):
    """Рассчитывает ожидаемую цену бургера."""
    return bun_price * 2 + sum(ingredient["price"] for ingredient in ingredients)


def get_parametrized_bun_data():
    """Возвращает данные для параметризации тестов булок."""
    return [(bun["name"], bun["price"]) for bun in TEST_BUNS]


def get_parametrized_ingredient_data():
    """Возвращает данные для параметризации тестов ингредиентов."""
    return [(ingredient["type"], ingredient["name"], ingredient["price"]) 
            for ingredient in TEST_INGREDIENTS[:3]]


def get_parametrized_burger_combinations():
    """Возвращает данные для параметризации тестов бургера."""
    return [
        (0, [0, 1]),
        (1, [2, 3]),
        (2, [4, 5])
    ]