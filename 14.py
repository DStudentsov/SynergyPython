#Задание 1

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_elements(lst, index=0):
    """
    Рекурсивно выводит элементы списка и завершающее сообщение.

    Параметры:
        lst (list): Список для обработки.
        index (int): Текущий индекс элемента (по умолчанию 0).
    """

    if index == len(lst):
        print("Конец списка")
        return

    print(lst[index])

    print_elements(lst, index + 1)

print("Начало списка:")
print_elements(my_list)