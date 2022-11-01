# Створення класу автомобіля з атрибутами та методами
class Car(object):
    """Class Car - goes """

    def __init__(self, color, brand, e_volume):
        self.color = color
        self.brand = brand
        self.e_volume = e_volume

    @staticmethod
    def ahead():
        """ The car goes ahead """
        return " - going ahead..."

    @staticmethod
    def back():
        """ The car goes back """
        return " - going back..."


class CarImproved(Car):

    @staticmethod
    def right():
        """ The car goes to the right """
        return " - going to the right..."

    @staticmethod
    def left():
        """ The car goes to the left """
        return " - going to the left..."
