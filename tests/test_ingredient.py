import pytest
from praktikum.ingredient import Ingredient
from tests.helpers.burger_helpers import get_parametrized_ingredient_data


class TestIngredient:
    
    @pytest.mark.parametrize('ingredient_type,name,price', get_parametrized_ingredient_data())
    def test_ingredient_creation_with_different_parameters(self, ingredient_type, name, price):
        """Тестирование создания ингредиента с разными параметрами."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
    
    def test_ingredient_get_price_returns_correct_value(self):
        """Тестирование метода get_price."""
        ingredient = Ingredient("SAUCE", "test sauce", 75.5)
        assert ingredient.get_price() == 75.5
    
    def test_ingredient_get_name_returns_correct_value(self):
        """Тестирование метода get_name."""
        ingredient = Ingredient("FILLING", "test filling", 100)
        assert ingredient.get_name() == "test filling"
    
    def test_ingredient_get_type_returns_correct_value(self):
        """Тестирование метода get_type."""
        ingredient = Ingredient("SAUCE", "test", 100)
        assert ingredient.get_type() == "SAUCE"