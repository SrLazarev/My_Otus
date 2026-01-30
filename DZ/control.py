import view
import model


def start_app():
    """Запуск программы"""
    phonebook = model.PhoneBook('phonebook.txt')
    running = True
    while running:
        try:
            view.show_menu()
            user_choice = view.input_data(view.input_choice)
            user_choice = int(user_choice)
            menu_items = [
                '',  # Заполнитель для индексации списка с единицы
                open_contacts,
                save_contacts,
                show_contacts,
                add_contacts,
                find_contacts,
                edit_contacts,
                delete_contacts,
                exit_program,
            ]

            # Если выбор пользователя совпадает с пунктом "Выход", останавливаем программу
            if user_choice == len(menu_items) - 1:
                running = False
                view.print_message(view.exit_message)
                continue

            menu_items[user_choice](phonebook)
        except IndexError:
            view.print_message(view.error_choice)
        except ValueError:
            view.print_message(view.error_choice)


def open_contacts(pb: model.PhoneBook):
    """Открытие телефонной книги."""
    pb.read_file()
    view.print_message(view.read_phonebook_successful)


def save_contacts(pb: model.PhoneBook):
    """Сохранение телефонной книги."""
    pb.save_file()
    view.print_message(view.save_phonebook_successful)


def show_contacts(pb: model.PhoneBook):
    """Показывает все контакты."""
    view.show_contact(pb.phonebook, view.error_empty_book)


def add_contacts(pb: model.PhoneBook):
    """Добавление нового контакта."""
    contact = view.input_data(view.input_add_contact)
    pb.add_contact(dict(zip(model.PhoneBook.FIELDS, contact)))  # Преобразуем список в словарь
    view.print_message(view.add_contact_successful.format(name=contact[0]))


def find_contacts(pb: model.PhoneBook):
    """Поиск контакта по ключевому слову."""
    search_word = view.input_data(view.input_search_word)
    result = pb.find_contact(search_word)
    view.show_contact(result, view.error_empty_find.format(word=search_word))


def edit_contacts(pb: model.PhoneBook):
    """Редактирование выбранного контакта."""
    id_edit = view.input_data(view.input_id_to_edit)
    if id_edit and id_edit.isdigit():
        id_edit = int(id_edit)
        if id_edit in pb.phonebook:
            edited_contact = view.input_data(view.input_edit_contact)
            contact_name = pb.edit_contact(id_edit, edited_contact)
            view.print_message(view.edit_contact_successful.format(name=contact_name))
        else:
            view.print_message(view.id_not_found)
    else:
        view.print_message(view.error_id_format)


def delete_contacts(pb: model.PhoneBook):
    """Удаление контакта по выбранному ID."""
    id_delete = view.input_data(view.input_id_to_delete)
    contact_name = pb.delete_contact(id_delete)
    view.print_message(view.delete_contact_successful.format(name=contact_name))


def exit_program(*args):
    """Завершение работы программы."""
    exit()