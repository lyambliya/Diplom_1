import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булки с настройкой поведения."""
    bun = Mock()
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    """Фикстура для создания мока ингредиента с настройкой поведения."""
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "test sauce"
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def complex_burger_setup():
    """Фикстура для создания бургера с предустановленными данными."""
    from praktikum.burger import Burger
    from praktikum.bun import Bun
    from praktikum.ingredient import Ingredient
    
    burger = Burger()
    bun = Bun("complex bun", 150)
    ingredient1 = Ingredient("SAUCE", "complex sauce", 75)
    ingredient2 = Ingredient("FILLING", "complex filling", 125)
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return {
        'burger': burger,
        'bun': bun,
        'ingredients': [ingredient1, ingredient2],
        'expected_price': 150 * 2 + 75 + 125
    }