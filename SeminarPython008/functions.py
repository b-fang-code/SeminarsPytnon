phone_book = []


def open_phone_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        print('Файл открыт ')
        return phone_book


def save_phone_book():
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(i)


def show_phone_book():
    print(phone_book)
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')))


def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append('\n' + user_info)


def change_phone_book():
    user_info = input('Введите номер контакта, которого Вы хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новый номер контакта: ')
            phone_book[i] =phone_book[i].replace(user_info, new_user_info)

def search_phone_book():
    user_info = input('Введите данные контакта, которые Вы хотите найти: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])


def delete_phone_book():
    user_info = input('Введите номер контакта, который вы хотите удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            phone_book.pop(i)
            break


phone_book = open_phone_book()
show_phone_book()
save_phone_book()
