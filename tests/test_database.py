import pytest
from unittest.mock import patch, Mock
from praktikum.database import Database
from tests.data.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestDatabase:
    
    def test_database_initialization(self):
        """Тестирование инициализации базы данных."""
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
    
    def test_available_buns_returns_correct_list(self):
        """Тестирование получения списка доступных булок."""
        database = Database()
        buns = database.available_buns()
        
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
    
    def test_available_ingredients_returns_correct_list(self):
        """Тестирование получения списка доступных ингредиентов."""
        database = Database()
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        assert ingredients[0].get_type() == "SAUCE"
    
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_creates_correct_objects_with_mocks(self, mock_ingredient, mock_bun):
        """Тестирование создания объектов в базе данных"""
        mock_bun_instance = Mock()
        mock_bun.return_value = mock_bun_instance
        
        mock_ingredient_instance = Mock()
        mock_ingredient.return_value = mock_ingredient_instance
        
        database = Database()
        
        assert mock_bun.call_count == 3
        assert mock_ingredient.call_count == 6
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        assert all(bun == mock_bun_instance for bun in database.buns)
        assert all(ingredient == mock_ingredient_instance for ingredient in database.ingredients)