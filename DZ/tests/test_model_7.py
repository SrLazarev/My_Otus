import pytest
from DZ.src.model import PhoneBook, ContactNotFoundError

def test_edit_non_existent_contact():
    """
    Тестирует обработку попыток обновить несуществующий контакт.
    Ожидается, что метод edit_contact вызовет исключение ContactNotFoundError.
    """
    # Создаем экземпляр PhoneBook
    book = PhoneBook("")
    book.phonebook = {
        1: {'name': 'Иван Иванов', 'phone': '+79111234567', 'city': 'Москва', 'address': 'ул. Ленина, д. 1', 'comment': 'Друзья'}
    }

    # Пробуем обновить несуществующий контакт
    with pytest.raises(ContactNotFoundError):
        book.edit_contact('999', ['', '', '', '', ''])  # Несуществующий ID