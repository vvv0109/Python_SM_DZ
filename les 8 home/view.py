import phone_book as pb

def main_menu ():
    print('Выберите команду меню:')
    print('1. Показать тел.книгу')
    print('2. загрузить тел.книгу')
    print('3. сохранить тел.книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('8. Выйти\n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice=int(input('Введите пункт меню: '))
            if choice in range (1,8) or choice==0:
                return choice
            else:
                print('Такого пункта нет')
        except:
            print('Ошибка ввода')
def print_phone_book():
    phone_book=pb.get_phone_book()
    print()
    if len(phone_book)<1:
        print('Тел.книга пуста\n')
    else:
        for id, contact in enumerate (phone_book, 1):
            print(id,*contact)
    print()
def input_new_contact():
    name=input('Введите имя: ')
    phone = input('Введите тел: ')
    comment = input('Введите комментарий контакта: ')
    print('Контакт сохранен в буфер обмена, не забудь сохранить книгу!\n')
    new_contact = [name,phone,comment]
    return new_contact
def input_remowe_contact():
    print()
    print_phone_book()
    id=int(input('Введите ИД контакта который удалить: '))
    return id
def input_change_contact():
    print()
    print_phone_book()
    id=int(input('Введите ИД контакта который изменть: '))
    return id
def input_search_contact():
    print()
    search = str(input('Введите значение поиска: '))
    return search



