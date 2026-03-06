def show_menu():
    """Отображение меню"""
    for i, item in enumerate(menu_items):
        if i != 0:
            print(f"\t{i}. {item}")
        else:
            print(item)


def input_data(message: str | tuple[str, ...]) -> str | list[str]:
    """
    Функция ввода данных от пользователя.

    :param message: Сообщение или кортеж сообщений для вывода
    :return: Введённые данные (одна строка или список строк)
    """
    result = []
    if isinstance(message, str):
        message = (message,)
    for input_message in message:
        result.append(input(input_message))
    return result[0] if len(result) == 1 else result


def show_contact(
    phonebook: dict[int, dict[str, str]],
    message_error: str
) -> None:
    """
    Показывает контакты из телефонной книги.

    :param phonebook: Телефонная книга (словарь контактов)
    :param message_error: Сообщение об ошибке при отсутствии записей
    """
    if phonebook:
        print("\nПеречень доступных контактов\n")
        print("     ID  Name        Phone           City        Address             Comment")
        for idx, contact in phonebook.items():
            print(
                f"\t{idx:>3}. "
                f"{contact['name']:<12}"
                f"{contact['phone']:<16}"
                f"{contact['city']:<12}"
                f"{contact['address']:<20}"
                f"{contact['comment']:<60}"
            )
        print()
    else:
        print_message(message_error)


def print_message(message: str) -> None:
    """
    Выводит сообщение в красивой рамке.

    :param message: Текст сообщения
    """
    print("\n┌" + "─" * (len(message) + 2) + "┐")
    print(f"│ {message} │")
    print("└" + "─" * (len(message) + 2) + "┘\n")


# Меню приложения
menu_items = [
    "Главное меню",
    "Открыть файл",
    "Сохранить файл",
    "Показать контакты",
    "Создать контакт",
    "Найти контакт",
    "Изменить контакт",
    "Удалить контакт",
    "Выход",
]

# Сообщения интерфейса
add_contact_successful = "Контакт {name} успешно добавлен!"
read_phonebook_successful = "Телефонная книга успешно открыта"
save_phonebook_successful = "Телефонная книга сохранена"
new_contact_successful = "Контакт {name} успешно создан"
edit_contact_successful = "Контакт '{name}' успешно изменён"
delete_contact_successful = "Контакт '{name}' успешно удалён"

input_choice = "Выберите пункт меню:"
input_add_contact = (
    "Введите имя:",
    "Введите номер телефона:",
    "Введите город проживания:",
    "Введите адрес:",
    "Введите комментарий:",
)
input_search_word = "Введите слово для поиска: "
input_id_to_edit = "Введите ID для изменения: "
input_id_to_delete = "Введите ID контакта для удаления: "
input_edit_contact = [
    "Введите новое имя для изменения контакта:",
    "Введите новый номер телефона для изменения контакта:",
    "Введите новый город проживания для изменения контакта:",
    "Введите новый адрес для изменения контакта:",
    "Введите новый комментарий для изменения контакта:",
]



# Сообщения об ошибках
error_choice = "Ошибка выбора пункта меню."
error_id_format = "Неверный формат ID."
error_empty_find = "Контакты, содержащие '{word}', не найдены"
error_empty_book = "Телефонная книга пуста или не открыта"
id_not_found = "Контакт с указанным ID не найден."
message_error = "eRRoR"


exit_message = "Вы вышли из программы! До новых встреч!"

