# Задание 1

pets = {}

name = input("Введите кличку питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner
}

for pet_name, data in pets.items():
     values = list(data.values())
     animal_type = values[0]
     age = values[1]
     owner = values[2]

     if age %10 == 1 and age % 100 !=11:
          age_str = f"{age} год"
     elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100>= 20):
          age_str = f"{age} года"
     else:
          age_str = f"{age} лет"

     result = f'Это {animal_type} по кличке "{pet_name}". Возраст питомца: {age_str}. Имя владельца: {owner}'

print(result)



# Задание 2

numbers = list(range(10, 0, -1)) + list(range(-1, -6, -1))

my_dict = {
    num: num ** num
    for num in numbers
}

print({
    10: my_dict[10],
    9: my_dict[9],
    "...": "...",
    -5: my_dict[-5]
})