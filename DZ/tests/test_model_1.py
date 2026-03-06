from DZ.src.model import PhoneBook, ReadFileError
import os
import tempfile
import pytest


@pytest.fixture
def temp_file():
 """
 Временный файл для тестирования чтения и записи.
 """
 fd, path = tempfile.mkstemp(text=True)
 try:
    yield path
 finally:
    os.close(fd)
    os.remove(path)


def test_read_existing_file(temp_file):
 """
 Тестирует чтение существующего файла с контактами.
 """
 # Заполняем временный файл данными
 with open(temp_file, "w", encoding="utf-8") as f:
    f.write(
    " иван иванов ;123;spb;nevsky;note\n"
    "petr petrov;456;msk;tverskaya;-\n"
    )

 # Создаём экземпляр PhoneBook и считываем данные
 book = PhoneBook(temp_file)
 book.read_file()

 # Проверяем, что количество контактов равно 2
 assert len(book) == 2

 # Проверяем данные первого контакта
 assert book.phonebook[1]["name"] == "Иван Иванов"
 assert book.phonebook[1]["phone"] == "123"

 # Проверяем данные второго контакта
 assert book.phonebook[2]["name"] == "Petr Petrov"
 assert book.phonebook[2]["city"] == "msk"