import pytest
from DZ.src.model import PhoneBook, ContactNotFoundError

@pytest.fixture
def manager(tmp_path):
    """
    Фикстура для создания экземпляра менеджера контактов
    """
    temp_file = tmp_path / "contacts.csv"
    book = PhoneBook(temp_file.as_posix())
    # Предварительное добавление тестового контакта
    book.add_contact({
        'name': 'Иван Иванов',
        'phone': '+79111234567',
        'city': 'Москва',
        'address': 'Ленинский проспект, д. 1',
        'comment': 'Хороший парень'
    })
    yield book

def test_delete_contact(manager):
    """
    Тестируем удаление контакта.
    """
    # Проверка успешного удаления
    deleted_name = manager.delete_contact('1')
    assert deleted_name == 'Иван Иванов'
    assert len(manager.phonebook) == 0

    # Проверка удаления несуществующего контакта
    with pytest.raises(ContactNotFoundError):
        manager.delete_contact('999')