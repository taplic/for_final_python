import model
import notes_app
import view


number = 1
# минимальное количество знаков в тексте заметки


def add():
    note = view.create_note(number)
    array = model.read_file()
    for notes in array:
        if notes_app.Note.get_id(note) == notes_app.Note.get_id(notes):
            notes_app.Note.set_id(note)
    array.append(note)
    model.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = model.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notes_app.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notes_app.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notes_app.Note.get_date(notes):
                print(notes_app.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = model.read_file()
    logic = True
    for notes in array:
        if id == notes_app.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = view.create_note(number)
                notes_app.Note.set_title(notes, note.get_title())
                notes_app.Note.set_body(notes, note.get_body())
                notes_app.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(notes_app.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    model.write_file(array, 'a')
