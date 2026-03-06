import pytest
from DZ.src.model import PhoneBook, SaveFileError

def test_save_file_with_incorrect_data(tmp_path):
    """
    Тестирует реакцию на попытку сохранения некорректных данных.
    Возбуждение исключение SaveFileError.
    """
    # Создаем временный файл
    temp_file = tmp_path / "contacts.csv"

    # Создаем экземпляр PhoneBook
    book = PhoneBook(temp_file.as_posix())

    # Формируем некорректные данные (недостаточно полей)
    book.phonebook = {
        1: {'name': 'Иван Иванов'}  # Недостающие поля city, address, comment
    }

    # Проверяем, что при попытке сохранения плохих данных возбуждается исключение
    with pytest.raises(SaveFileError):
        book.save_file()