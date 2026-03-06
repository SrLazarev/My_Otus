import io
from unittest.mock import patch
from DZ.src.view import show_contact, print_message

def test_show_contact_empty_calls_print_message(monkeypatch):
    # Подмена функции print_message
    calls = []
    def mock_print_message(message):
        calls.append(message)

    monkeypatch.setattr("DZ.src.view.print_message", mock_print_message)

    # Тест с пустым телефонным справочником
    phonebook = {}
    show_contact(phonebook, "Телефонная книга пуста")
    assert calls == ["Телефонная книга пуста"], "Ожидалось, что будет вызвано print_message с нужным сообщением"

    # Очистим накопленные вызовы
    del calls[:]

    # Тест с ненулевым телефонным справочником
    phonebook = {1: {'name': 'Иван Иванов', 'phone': '+79111234567', 'city': 'Москва', 'address': 'ул. Ленина, д. 1', 'comment': 'Друзья'}}
    show_contact(phonebook, "")
    assert calls == [], "Ожидалось, что print_message не будет вызываться при наличии контактов"