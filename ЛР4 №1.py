class Square:
    def __init__(self, side):
        self.side = side

    def periment(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def diagonal(self):
        return self.side * (2 ** 0.5)

square = Square(5)

print("Периметр:", square.periment())
print("Площадь:", square.area())
print("Диагональ:", round(square.diagonal(), 2))