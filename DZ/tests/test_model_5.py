import pytest
from DZ.src.model import PhoneBook, ReadFileError

def test_read_file_when_file_is_missing(tmp_path):
    """
    Тестирует реакцию на отсутствие файла при вызове метода read_file.
    Должно возбудиться исключение ReadFileError.
    """
    # Генерируем путь к несуществующему файлу
    fake_file_path = tmp_path / "nonexistent_file.csv"

    # Создаем экземпляр PhoneBook с несуществующим путем
    book = PhoneBook(fake_file_path.as_posix())

    # Пробуем считать файл и убеждаемся, что возбуждается исключение
    with pytest.raises(ReadFileError):
        book.read_file()