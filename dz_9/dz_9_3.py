# Програма вираховує площу прямокутника та квадрата
class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Square(Parallelogram):
    def get_area(self):
        return self.width ** 2


rectangle = Parallelogram(5, 4)
print(f'Area of rectangle = {rectangle.get_area()}')
square = Square(10, 10)
print(f'Area of square = {square.get_area()}')
