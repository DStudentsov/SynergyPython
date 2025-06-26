# Задание 1

def factorial(n):
    """Вычисляет факториал числа n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def get_factorial_list(num):
    """Создает список факториалов от факториала num до 1."""
    start = factorial(num)
    return [factorial(n) for n in range(start, 0, -1)]

print(get_factorial_list(3))


# Задание 2

import collections

pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}},
}

def get_suffix(age):
    """
    Определяет правильное склонение для возраста.
    Пример: 1 → 'год', 3 → 'года', 25 → 'лет'
    """
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Возвращает данные питомца по ID или False, если не найден"""
    return pets.get(ID, False)

def create():
    """Добавляет новую запись в базу данных"""
    if not pets:
        new_id = 1
    else:
        last_id = collections.deque(pets, maxlen=1)[0]
        new_id = last_id + 1

    name = input("Введите кличку питомца: ").strip()

    while True:
        animal_type = input("Введите вид питомца: ").strip()
        if any(char.isdigit() for char in animal_type):
            print("Ошибка: вид не должен содержать цифр!")
        else:
            break

    while True:
        try:
            age = int(input("Введите возраст питомца: "))
            if age < 0:
                print("Ошибка: возраст не может быть отрицательным!")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое число!")

    owner = input("Введите имя владельца: ").strip()

    pets[new_id] = {name: {
        "Вид питомца": animal_type,
        "Возраст питомца": age,
        "Имя владельца": owner
    }}
    print(f"Питомец добавлен с ID {new_id}")

def read():
    """Выводит информацию о питомце по ID"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    pet_name = next(iter(pet.keys()))
    data = pet[pet_name]
    age_str = f"{data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}"

    print(f'Это {data["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {age_str}. Имя владельца: {data["Имя владельца"]}')

def update():
    """Редактирует существующую запись"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    pet_name = next(iter(pet.keys()))
    print("Введите новые данные (оставьте пустым, чтобы не изменять):")

    new_type = input(f"Вид питомца ({pet[pet_name]['Вид питомца']}): ").strip()
    if new_type:
        if any(char.isdigit() for char in new_type):
            print("Ошибка: вид не должен содержать цифр!")
        else:
            pet[pet_name]["Вид питомца"] = new_type

    while True:
        new_age = input(f"Возраст питомца ({pet[pet_name]['Возраст питомца']}): ").strip()
        if not new_age:
            break
        try:
            new_age = int(new_age)
            if new_age < 0:
                print("Ошибка: возраст не может быть отрицательным!")
            else:
                pet[pet_name]["Возраст питомца"] = new_age
                break
        except ValueError:
            print("Ошибка: введите целое число!")

    new_owner = input(f"Имя владельца ({pet[pet_name]['Имя владельца']}): ").strip()
    if new_owner:
        pet[pet_name]["Имя владельца"] = new_owner

    print("Данные обновлены")

def delete():
    """Удаляет запись из базы"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    if ID not in pets:
        print("Питомец с таким ID не найден")
        return

    del pets[ID]
    print("Питомец удален")

def pets_list():
    """Выводит список всех питомцев"""
    if not pets:
        print("База данных пуста")
        return

    for ID, pet in pets.items():
        pet_name = next(iter(pet.keys()))
        data = pet[pet_name]
        age_str = f"{data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}"
        print(f"[ID: {ID}]: {pet_name}, Вид: {data['Вид питомца']}, Возраст: {age_str}, Владелец: {data['Имя владельца']}")

while True:
    command = input("\nВведите команду (create/read/update/delete/list/stop): ").strip().lower()

    if command == "stop":
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print("Неизвестная команда")

print("Работа программы завершена")