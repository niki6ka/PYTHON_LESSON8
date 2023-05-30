# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать тк
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

path = "phonebook.txt"


def delete(contacts):
    print("Введите контакт: ")
    name = input('> ')
    for contact in contacts:
        if contact['name'] == name:
            print("Вы хотите удалить контакт %s (yes/no)?: " % name)
            name_del = input('> ')
            if name_del == 'yes':
                contacts.remove(contact)
                print("Вы удалили контакт %s " % name)


def change_contact_file():
    with open(path, 'r+', encoding='UTF-8') as file1:
        data_list = []
        finding_contact = str(input("Введите искомый параметр (имя, фамилию, отчество или телефон: "))
        for line in file1:
            data_list.append(line.strip())

        for i in data_list:
            res = i.split()
            if res[0] == finding_contact or res[1] == finding_contact \
                    or res[2] == finding_contact or res[3] == finding_contact:
                print(f'\n')
                print(i)
                change_cont = input("Вы хотите заменить этот контакт (Y/N)?: ")
                if change_cont == 'Y':
                    data_list.remove(i)
                    adding_into_file()
                print(f'\n')
    file1.close()
    main_func()


def finding_contact_file():
    with open(path, 'r+', encoding='UTF-8') as file1:
        data_list = []
        finding_contact = str(input("Введите искомый параметр (имя, фамилию, отчество или телефон: "))
        for line in file1:
            data_list.append(line.strip())

        for i in data_list:
            res = i.split()
            if res[0] == finding_contact or res[1] == finding_contact \
                    or res[2] == finding_contact or res[3] == finding_contact:
                print(f'\n')
                print(i)
                print(f'\n')

    main_func()


# def finding_contact_file():
#   data = open(path, 'r', encoding="UTF-8")
#    finding_contact = input("Введите искомый параметр: ")
#    in_finding_text = data.readlines()
#    dict_contacts = {}
#   for i, j in enumerate(in_finding_text, 1):
#       j = j.strip()
#        dict_contacts = {"name": in_finding_text[0], "middle_name": in_finding_text[1], "surname": in_finding_text[2],
#                         "phone": in_finding_text[3]}

#   for i in in_finding_text:
#       if i == finding_contact:
#           print(dict_contacts[])


def save_file():
    data = open(path, 'a', encoding="UTF-8")
    data.close()


def clear_all():
    data = open('phonebook.txt', 'w', encoding='UTF-8')
    data.write('')


def create_file():
    data = open(path, 'a', encoding="UTF-8")
    data.close()


def reading_file():
    data = open(path, 'r', encoding="UTF-8")
    print(data.read())
    print(f'\n')
    data.close()
    main_func()


def open_file():
    data = open(path, 'r', encoding="UTF-8")
    data.close()


def adding_into_file():
    data = open(path, 'a', encoding="UTF-8")
    name = input("Введите имя: ").capitalize()
    middle_name = input("Введите отчество: ").capitalize()
    surname = input("Введите фамилию: ").capitalize()
    phone = input("Введите номер телефона: ")
    data.write(f"\n{name} {middle_name} {surname} {phone}")
    print(f"\nКонтакт: {name} {middle_name} {surname} {phone} - Успешно добавлен!\n")
    data.close()
    main_func()


def main_func():
    print('1. Открыть файл')
    print('2. Сохранить файл')
    print('3. Показать телефонную книгу')
    print('4. Добавить контакт')
    print('5. Найти контакт')
    print('6. Изменить контакт')
    print('7. Удалить контакт')
    print('8. Выход')

    while True:
        menu = int(input('Введите номер необходимого действия: '))
        if menu == 8:
            print("До новых встреч!!!")
            break

        elif menu == 1:
            open_file()
        elif menu == 2:
            save_file()
        elif menu == 3:
            reading_file()
        elif menu == 4:
            adding_into_file()
        elif menu == 5:
            finding_contact_file()
        elif menu == 6:
            change_contact_file()


main_func()

# adding_into_file()
