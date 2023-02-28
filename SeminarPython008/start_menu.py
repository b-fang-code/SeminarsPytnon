import functions as f
def print_menu():
    print('Это телефонный справочник. Выберите действие, которое нужно совершить: \n'
          '1. Открыть файл \n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакт\n'
          '5. Изменить контакт\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
    data = int(input('Введите номер необходимого действия: '))
    return data



while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print('Открыть файл')
            f.open_phone_book()
        case 2:
            print('Сохранить файл')
            f.save_phone_book()
        case 3:
            print('Показать контакты')
            f.show_phone_book()
        case 4:
            print('Добавить контакт')
            f.add_phone_book()
        case 5:
            print('Изменить контакт')
            f.change_phone_book()
        case 6:
            print('Найти контакт')
            f.search_phone_book()
        case 7:
            print('Удалить контакт')
            f.delete_phone_book()
        case 8:
            print('Выход')
            f.escape()
            break
