import view
from view import print_message

# Базовый класс всех исключений нашего приложения
class PhoneBookException(Exception):
    pass


# Исключение, возникающее при ошибке чтения файла
class ReadFileError(PhoneBookException):
    def __init__(self, message=None):
        super().__init__(message or 'Ошибка при чтении файла')


# Исключение, возникающее при ошибке сохранения файла
class SaveFileError(PhoneBookException):
    def __init__(self, message=None):
        super().__init__(message or 'Ошибка при сохранении файла')


# Исключение, возникающее при попытке изменить несуществующий контакт
class ContactNotFoundError(PhoneBookException):
    def __init__(self, contact_id):
        super().__init__(f'Контакт с id={contact_id} не найден')


class PhoneBook:
    SEPARATOR = ";"
    FIELDS = ["name", "phone", "city", "address", "comment"]


    @staticmethod
    def normalize_name(name):
        """Нормализует имя, приводя его к одному регистру и обрезая лишние пробелы."""
        return name.strip().title()


    def __init__(self, path: str):
        """
        Конструктор класса PhoneBook.
        :param path: путь к файлу телефонной книги
        """
        self.path = path
        self.phonebook = {}


    def __repr__(self):
        """Возвращает строковое представление телефонной книги."""
        return f"<PhoneBook: {len(self.phonebook)} contacts>"


    def __len__(self):
        """Возвращает количество контактов в телефонной книге."""
        return len(self.phonebook)


    def read_file(self):
        """
        Чтение телефонной книги из файла.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                idx = 1
                while line := file.readline().strip():
                    contact_data = line.split(self.SEPARATOR)
                    normalized_contact = {
                        field: value.strip()
                        for field, value in zip(self.FIELDS, contact_data)
                    }
                    normalized_contact["name"] = self.normalize_name(normalized_contact["name"])
                    self.phonebook[idx] = normalized_contact
                    idx += 1
        except FileNotFoundError:
            raise ReadFileError('Файл не найден') from None
        except Exception as e:
            raise ReadFileError(str(e)) from None


    def save_file(self):
        """
        Сохранение телефонной книги в файл.
        """
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                data = []
                for contact in self.phonebook.values():
                    data.append(self.SEPARATOR.join(list(contact.values())))
                data = "\n".join(data)
                file.write(data)
        except KeyError:
            raise SaveFileError('Некорректный формат данных') from None
        except Exception as e:
            raise SaveFileError(str(e)) from None


    def _next_id(self):
        """
        Возвращает следующий уникальный ID для контакта.
        """
        return len(self.phonebook) + 1


    def add_contact(self, contact_data: dict):
        """
        Добавляет новый контакт в телефонную книгу.

        :param contact_data: Данные контакта в виде словаря
        """
        idx = self._next_id()
        self.phonebook[idx] = contact_data


    def find_contact(self, word: str):
        """
        Поиск контакта по заданному слову.

        :param word: Слово для поиска
        :return: Словарь с результатами поиска
        """
        result = {}
        for idx, contact in self.phonebook.items():
            for value in contact.values():
                if word.lower() in value.lower():
                    result[idx] = contact
                    break
        return result


    def edit_contact(self, contact_id: str, new_contact_data: list[str]):
        """
        Редактирует указанный контакт.

        :param contact_id: Идентификатор контакта
        :param new_contact_data: Новые данные контакта
        :return: Имя обновленного контакта или None, если контакт не найден
        """
        try:
            contact_id = int(contact_id)
            if contact_id not in self.phonebook:
                raise ContactNotFoundError(contact_id)

            updated_fields = {}
            for i, field in enumerate(self.FIELDS):
                if new_contact_data[i]:
                    updated_fields[field] = new_contact_data[i].strip()
            self.phonebook[contact_id].update(updated_fields)
            return self.phonebook[contact_id]["name"]
        except ValueError:
            raise ContactNotFoundError(contact_id) from None
        except Exception as e:
            raise SaveFileError(str(e)) from None


    def delete_contact(self, contact_id: str):
        """
        Удаляет контакт по указанному идентификатору.

        :param contact_id: Идентификатор контакта
        :return: Имя удаленного контакта или None, если контакт не найден
        """
        try:
            contact_id = int(contact_id)
            if contact_id not in self.phonebook:
                print_message(view.id_not_found)
                return None
            deleted_contact = self.phonebook.pop(contact_id)
            return deleted_contact["name"]
        except Exception as e:
            raise SaveFileError(str(e)) from None