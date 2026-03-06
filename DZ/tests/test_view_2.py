from unittest.mock import patch
from DZ.src.view import input_data


@patch('builtins.input', side_effect=["John Doe", "1234567890"])
def test_input_data(mocked_input):
    """
    Тестирует функцию input_data с поддержкой ввода данных пользователем.
    """
    messages = ("Введите имя:", "Введите номер телефона:")
    user_inputs = input_data(messages)
    assert user_inputs == ["John Doe", "1234567890"]