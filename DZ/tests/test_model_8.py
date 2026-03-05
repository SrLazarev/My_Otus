import pytest
from DZ.src.model import PhoneBook, ContactNotFoundError

def test_raise_contact_not_found_error():
    """
    Тестирует подъем исключения ContactNotFoundError при работе с несуществующим контактом.
    """
    # Создаем экземпляр PhoneBook
    book = PhoneBook("")
    book.phonebook = {
        1: {'name': 'Иван Иванов', 'phone': '+79111234567', 'city': 'Москва', 'address': 'ул. Ленина, д. 1', 'comment': 'Друзья'}
    }

    # Пробуем обратиться к несуществующему контакту
    with pytest.raises(ContactNotFoundError):
        book.delete_contact('999')  # Несуществующий ID