# Створення свого класу виключення для виводу тексту на печать
class MyNewException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Помилка! -> {self.message}'


class Print:
    def printout(self, data):
        self.send_data(data)
        print(f"Печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise MyNewException("Прінтер не відповідає...")

    def send_to_print(self, data):
        return True


p = Print()
p.printout("Добрий вечір, ми з Ураїни!")
