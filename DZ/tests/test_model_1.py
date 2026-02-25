from DZ.src.model import PhoneBook, ReadFileError
import os
import tempfile
import pytest


@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(text=True)
    try:
        yield path
    finally:
        os.close(fd)
        os.remove(path)


def test_read_existing_file(temp_file):
    # пишем корректные данные телефонной книги
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(
            "  иван иванов ;123;spb;nevsky;note\n"
            "petr petrov;456;msk;tverskaya;-\n"
        )

    book = PhoneBook(temp_file)
    book.read_file()

    assert len(book) == 2
    assert book.phonebook[1]["name"] == "Иван Иванов"   # проверяем нормализацию имени
    assert book.phonebook[1]["phone"] == "123"
    assert book.phonebook[2]["name"] == "Petr Petrov"
    assert book.phonebook[2]["city"] == "msk"
