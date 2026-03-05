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

def test_edit_contact(manager):
    """
    Тестирует редактирование контакта.
    """
    # Проверка успешного редактирования
    edited_name = manager.edit_contact('1', ['Андрей Андреев', '+79211234567', 'Санкт-Петербург', 'Невский проспект, д. 1', 'Просто хороший парень'])
    assert edited_name == 'Андрей Андреев'
    assert manager.phonebook[1]['name'] == 'Андрей Андреев'
    assert manager.phonebook[1]['phone'] == '+79211234567'
    assert manager.phonebook[1]['city'] == 'Санкт-Петербург'
    assert manager.phonebook[1]['address'] == 'Невский проспект, д. 1'
    assert manager.phonebook[1]['comment'] == 'Просто хороший парень'

    # Проверка обработки несуществующего контакта
    with pytest.raises(ContactNotFoundError):
        manager.edit_contact('999', [' ', '', '', '', ''])

    # Проверка некорректного идентификатора (строка вместо числа)
    with pytest.raises(ContactNotFoundError):
        manager.edit_contact('abc', [' ', '', '', '', ''])