import phone_book as pb
path= r'phone_book.txt'
def load_contacts()->list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data=file.readlines()
    pb.set_phone_book(str_to_list(data))
    print('Тел.книга ЗАГРУЖЕНА!\n')
def save_contacts():
    global path
    rady_book=list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(rady_book)
    print('Тел.книга Сохранена!\n')
def list_to_str(phone_book: list)->str:
    str_phone_book =''
    for contact in phone_book:
        new_contact=';'.join(contact)
        str_phone_book +=new_contact+'\n'
    return str_phone_book[:-2]

def str_to_list(phone_book: list) -> list:
    new_lisst=[]
    for contact in phone_book:
        new_contact=contact.strip().split(';')
        new_lisst.append( new_contact)
    return new_lisst
