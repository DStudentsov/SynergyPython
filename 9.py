# Задание 1
try:
    n = int(input("Введите количество чисел (1 ≤ N ≤ 100000): "))
    if n < 1 or n > 100000:
        raise ValueError("N должно быть в диапазоне от 1 до 100000.")
except ValueError as e:
    print(f"Ошибка: {e}")
    exit()

numbers_str = input("Введите числа через пробел: ").split()
if len(numbers_str) != n:
    print(f"Ошибка: Введено {len(numbers_str)} чисел вместо {n}.")
    exit()

try:
    numbers = list(map(int, numbers_str))
except ValueError:
    print("Ошибка: Введены некорректные данные (не целые числа).")
    exit()

for num in numbers:
    if abs(num) > 2 * 10**9:
        print(f"Ошибка: Число {num} превышает 2*10^9 по модулю.")
        exit()

unique_numbers = set(numbers)
print("Количество уникальных чисел:", len(unique_numbers))


# Задание 2
print("Введите числа первого списка (каждое на новой строке). Для завершения ввода нажмите Enter:")
list1 = []
while True:
    line = input().strip()
    if line == "":
        break
    try:
        num = int(line)
        list1.append(num)
    except ValueError:
        print(f"Ошибка: '{line}' не является целым числом. Пожалуйста, вводите только целые числа.")
        exit()

print("\nВведите числа второго списка (каждое на новой строке). Для завершения ввода нажмите Enter:")
list2 = []
while True:
    line = input().strip()
    if line == "":
        break
    try:
        num = int(line)
        list2.append(num)
    except ValueError:
        print(f"Ошибка: '{line}' не является целым числом. Пожалуйста, вводите только целые числа.")
        exit()

set1 = set(list1)
set2 = set(list2)

common_numbers = set1 & set2

print("\nРезультат:")
print(len(common_numbers))


# Задание 3
numbers_input = input("Введите числа через пробел (например: 1 2 3 2 3 4): ").split()
seen_numbers = set()
results = []

for num_str in numbers_input:
    try:
        num = int(num_str)
    except ValueError:
        try:
            num = float(num_str)
        except ValueError:
            print(f"Ошибка: '{num_str}' не является числом.")
            exit()
    if num in seen_numbers:
        results.append("YES")
    else:
        results.append("NO")
        seen_numbers.add(num)

print("\n".join(results))