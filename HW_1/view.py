import notes_app


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Текст заметки: '), number)
    return notes_app.Note(title=title, body=body)


def menu():
    print("\nДобрый день! Это приложение 'Заметки'. Имеются следующие воэможности:\n\n1 - показать все заметки \n2 - добавить заметку\n3 - удалить заметку\n4 - редактировать заметку\n5 - выбрать заметку по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер команды: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Удачного дня! До скорой встречи!")
