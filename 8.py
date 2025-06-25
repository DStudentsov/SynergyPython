# Задание 1

N = int(input("Введите количество чисел N (1 ≤ N ≤ 10000): "))

if N < 1 or N > 10000:
    print("Ошибка: N должно быть в диапазоне от 1 до 10000.")
else:
    numbers = []
    for i in range(N):
        number = int(input(f"Введите число {i + 1} (по модулю не больше 10^5): "))
        if abs(number) > 10**5:
            print("Ошибка: Число должно быть по модулю не больше 10^5.")
            break
        else:
            numbers.append(number)
    else:
        reversed_numbers = numbers[::-1]

        print("Перевернутый массив:", ' '.join(map(str, reversed_numbers)))


# Задание 2

n = int(input("Введите количество элементов массива (N): "))
arr = input("Введите элементы массива через пробел: ").split()
result = [arr[-1]] + arr[:-1]

print(' '.join(result))


# Задание 3

def min_boats_needed(max_weight, num_fishers, weights):
    weights.sort()
    left = 0
    right = num_fishers - 1
    boats_count = 0

    while left <= right:
        if weights[left] + weights[right] <= max_weight:
            left += 1
            right -= 1
            boats_count += 1
    return boats_count

if __name__ == "__main__":
    m = int(input("Введите максимальный вес лодки: "))
    n = int(input("Введите количество рыбаков: "))
    weights = []

    for _ in range(n):
        weight = int(input("Введите вес рыбака: "))
        weights.append(weight)

    result = min_boats_needed(m, n, weights)
    print(result)