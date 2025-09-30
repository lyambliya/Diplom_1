import pytest
from praktikum.bun import Bun
from tests.helpers.burger_helpers import get_parametrized_bun_data


class TestBun:
    
    @pytest.mark.parametrize('name,price', get_parametrized_bun_data())
    def test_bun_creation_with_different_parameters(self, name, price):
        """Тестирование создания булочки с разными параметрами."""
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        assert bun.get_price() == price
    
    def test_bun_get_name_returns_correct_value(self):
        """Тестирование метода get_name."""
        bun = Bun("test bun", 100)
        assert bun.get_name() == "test bun"
    
    def test_bun_get_price_returns_correct_value(self):
        """Тестирование метода get_price."""
        bun = Bun("test bun", 150.5)
        assert bun.get_price() == 150.5