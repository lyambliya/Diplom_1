import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.helpers.burger_helpers import (
    create_test_burger_with_ingredients, 
    calculate_expected_price,
    get_parametrized_burger_combinations
)
from tests.data.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestBurger:
    
    def test_burger_initialization(self):
        """Тестирование инициализации бургера."""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns(self, mock_bun):
        """Тестирование установки булок."""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self, mock_ingredient):
        """Тестирование добавления ингредиента."""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self):
        """Тестирование удаления ингредиента."""
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "sauce1", 100)
        ingredient2 = Ingredient("FILLING", "filling1", 200)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2
    
    def test_move_ingredient(self):
        """Тестирование перемещения ингредиента."""
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "sauce1", 100)
        ingredient2 = Ingredient("FILLING", "filling1", 200)
        ingredient3 = Ingredient("SAUCE", "sauce2", 300)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient3
        assert burger.ingredients[2] == ingredient1
    
    @pytest.mark.parametrize('bun_index,ingredient_indices', get_parametrized_burger_combinations())
    def test_get_price_with_different_combinations(self, bun_index, ingredient_indices):
        """Тест расчета цены с разными комбинациями."""
        bun_data = TEST_BUNS[bun_index]
        ingredients_data = [TEST_INGREDIENTS[i] for i in ingredient_indices]
        
        burger = create_test_burger_with_ingredients(bun_data, ingredients_data)
        expected_price = calculate_expected_price(bun_data["price"], ingredients_data)
        
        assert burger.get_price() == expected_price
    
    def test_get_receipt_format(self):
        """Тестирование формата чека."""
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient1 = Ingredient("SAUCE", "hot sauce", 100)
        ingredient2 = Ingredient("FILLING", "cutlet", 200)
        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        assert f"(==== {bun.get_name()} ====)" in lines[0]
        assert "= sauce hot sauce =" in lines[1]
        assert "= filling cutlet =" in lines[2]
        assert f"(==== {bun.get_name()} ====)" in lines[3]
        assert f"Price: {burger.get_price()}" in lines[5]
    
    def test_complex_burger_scenario(self, complex_burger_setup):
        burger = complex_burger_setup['burger']
        expected_price = complex_burger_setup['expected_price']
        
        assert burger.get_price() == expected_price
        assert len(burger.ingredients) == 2