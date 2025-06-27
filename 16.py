#Задание 1

class CashRegister:
    def __init__(self, initial=0):
        self.money = initial

    def top_up(self, X):
        """Пополнить кассу на сумму X."""
        self.money += X

    def take_away(self, X):
        """Изъять сумму X из кассы. Вызывает ошибку при недостатке средств."""
        if self.money < X:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= X

    def count_1000(self):
        """Возвращает количество целых тысяч в кассе."""
        return self.money // 1000

kassa = CashRegister(5500)
kassa.top_up(500)
print(kassa.count_1000())
kassa.take_away(3000)

#Задание 2

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        """Двигаться вверх по оси Y."""
        self.y += self.s

    def go_down(self):
        """Двигаться вниз по оси Y."""
        self.y -= self.s

    def go_left(self):
        """Двигаться влево по оси X."""
        self.x -= self.s

    def go_right(self):
        """Двигаться вправо по оси X."""
        self.x += self.s

    def evolve(self):
        """Увеличить размер шага на 1."""
        self.s += 1

    def degrade(self):
        """Уменьшить размер шага. При s <= 0 вызывает ошибку."""
        if self.s <= 1:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """Вычисляет минимальное количество шагов до точки (x2, y2)."""
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        steps_x = (dx + self.s - 1) // self.s if dx != 0 else 0
        steps_y = (dy + self.s - 1) // self.s if dy != 0 else 0
        return steps_x + steps_y

"""
Пояснение к классу Turtle:
1. __init__: задает стартовую позицию (x, y) и размер шага s.
2. Методы go_up/down/left/right: меняют координаты на s единиц.
3. evolve/degrade: управляют размером шага с проверкой на s > 0.
4. count_moves: вычисляет минимальные шаги через деление с округлением вверх.
"""

turtle = Turtle(0, 0, 2)
turtle.go_right()
turtle.go_up()
print(turtle.count_moves(5, 3))
turtle.evolve()
print(turtle.count_moves(5, 3))