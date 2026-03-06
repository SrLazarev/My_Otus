import pytest

from DZ.src.model import PhoneBook

@pytest.fixture
def manager(tmp_path):
    """
    Фикстура для создания экземпляра менеджера контактов
    """
    temp_file = tmp_path / "contacts.json"
    book = PhoneBook(temp_file.as_posix())
    # Предварительная запись тестовых контактов
    book.phonebook = {
        1: {'name': 'Ivanov Ivan',
            'phone': '+79111234567',
            'city': 'Feodosia',
            'address': 'lenina',
            'comment': 'frend'
            },
        2: {'name': 'Ann',
            'phone': '+79217654321',
            'city': 'kerch',
            'address': 'zaliv',
            'comment': 'frend'
            },
    }
    yield book
    book.save_file()  # сохраняем изменения после завершения теста

def test_search_by_field(manager):
    """
    Тестирует поиск контактов по различным полям.
    """
    # Поиск по имени
    result = manager.find_contact('Ivanov')
    assert len(result) > 0, "Контакт не найден по имени"
    assert any('Ivanov Ivan' in contact['name'] for contact in result.values()), "Несоответствие имен"

    # Поиск по номеру телефона
    result_phone = manager.find_contact('+79217654321')
    assert len(result_phone) > 0, "Контакт не найден по номеру телефона"
    assert any('+79217654321' in contact['phone'] for contact in result_phone.values()), "Несоответствие номера телефона"

    # Поиск по городу
    result_phone = manager.find_contact('kerch')
    assert len(result_phone) > 0, "Контакт не найден по городу"
    assert any('kerch' in contact['city'] for contact in result_phone.values()), "Несоответствие города"

    # Поиск по адресу
    result_phone = manager.find_contact('zaliv')
    assert len(result_phone) > 0, "Контакт не найден по городу"
    assert any('zaliv' in contact['address'] for contact in result_phone.values()), "Несоответствие адреса"

    # Поиск несуществующего контакта
    empty_result = manager.find_contact('Некое Имя')
    assert not empty_result, "Вернулся контакт при отсутствии совпадений"