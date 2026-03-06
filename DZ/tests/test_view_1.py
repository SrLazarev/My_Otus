import io
import sys
from unittest.mock import patch
from DZ.src.view import show_menu, menu_items

def test_show_menu():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    show_menu()
    output = captured_output.getvalue().strip()
    expected_output = menu_items[0] + ''.join([
        f"\n\t{i}. {item}" for i, item in enumerate(menu_items[1:], start=1)
    ])
    assert output == expected_output
    sys.stdout = sys.__stdout__