import view
import data_base
phone_book=[]
def get_phone_book()->list:
    global phone_book
    return phone_book
def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book=new_phone_book
def add_contact():
    global  phone_book
    contact=view.input_new_contact()
    phone_book.append(contact)
def remove_contact():
    global phone_book
    id=view.input_remowe_contact()
    confirm=input(f'Удалить?{phone_book[id-1][0]}? (y/n)')
    if confirm.lower()=='y':
        del_contact=phone_book.pop(id-1)
def change_contact():
    global phone_book
    id=view.input_change_contact()
    confirm=input(f'Изменить?{phone_book[id-1][:]}? (y/n)')
    if confirm.lower()=='y':
        del_contact=phone_book.pop(id-1)
        view.input_new_contact
        contact = view.input_new_contact()
        phone_book.append(contact)
def search_contact():
    searchname = input("Введи значение поиска: ")
    searchname=searchname.lower()
    myfile = open('phone_book.txt', 'r', encoding='UTF-8')
    filecontents = myfile.readlines()
    found = False
    for line in filecontents:
        if searchname in line:
            print("Твоя запись:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("Такого нет", searchname)





