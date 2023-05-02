# Напишите информационную систему «Сотрудники». Программа должна обеспечивать ввод данных,
# редактирование данных сотрудника, удаление сотрудника, поиск сотрудника по фамилии,
# вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл.
# Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически,
# в процессе исполнения программы — по команде пользователя). При старте программы происходит загрузка
# списка сотрудников из указанного пользователем файла.

# with open('file.txt', 'r', encoding='utf-8') as f:
#     str = f.read()
#     person = dict(i.split(':') for i in str.split(','))
#     print(person)

person = {'Иванов Иван Иванович': 25, 'Степанов Степан Степанович': 20}

def funk_add():
    name = input("Введите ФИО, которое необходимо добавить: ")
    age = int(input("Введите возраст: "))
    person.update({name: age})
    print(person)


def funk_delete():
    name = input('Введите ФИО, которое необходимо удалить: ')
    person.pop(name)
    print(person)


def funk_edit():
    print(person)
    answer = int(input('Выберите действие (0 - для изменения ФИО и возраста, 1 - для изменения возраста): '))

    if answer == 0:
        old_name = input('Старое ФИО: ')
        new_name = input('Новое ФИО: ')
        new_age = int(input('Введите возраст: '))
        person[new_name] = person.pop(old_name)
        person[new_name] = new_age
        print(person)

    elif answer == 1:
        name = input('Введите ФИО, у которого необходимо изменить возраст: ')
        new_age = int(input('Введите новый возраст: '))
        person[name] = new_age
    print(person)


def funk_find():
    print(person)
    name2 = input('Введите фамилию для поиска: ')
    for i in person.items():
        if name2 == i[0][:len(name2)]:
            print(i)
            with open('file.txt', 'w', encoding='utf-8') as f:
                result = str(i)
                f.write(result)

def age_find():
    print(person)
    age2 = int(input('Введите возраст для поиска: '))
    for i, j in person.items():
        if j == age2:
            print(i)
            with open('file.txt', 'w', encoding='utf-8') as f:
                result = str(i)
                f.write(result)

def letter_find():
    print(person)
    letter = input('Введите букву: ')
    for i in person:
        if i[0] == letter:
            print(i)
            with open('file.txt', 'w', encoding='utf-8') as f:
                result = str(i)
                f.write(result)

def save():
    with open('file.txt', 'w', encoding='utf-8') as f:
        result = str(person)
        f.write(result)


while True:
    menu = ('Добавить', 'Удалить', 'Изменить', 'Найти по фамилии', 'Найти по возрасту',
            'Найти по первой букве Фамилии', 'Сохранить список сотрудников в файл')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print()

    x = int(input('Выберите действие, которое вы хотите выполнить: '))
    if x == 1:
        funk_add()
    elif x == 2:
        funk_delete()
    elif x == 3:
        funk_edit()
    elif x == 4:
        funk_find()
    elif x == 5:
        age_find()
    elif x == 6:
        letter_find()
    elif x == 7:
        save()
    else:
        with open('file.txt', 'w', encoding='utf-8') as f:
            result = str(person)
            f.write(result)
        break
