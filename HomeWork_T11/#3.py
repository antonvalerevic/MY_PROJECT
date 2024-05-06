# Программа с классом Car. При инициализации объекта
# ему должны задаваться атрибуты color, type и year.
# Реализовать пять методов. Запуск автомобиля – выводит
# строку «Автомобиль заведён». Отключение автомобиля –
# выводит строку «Автомобиль заглушен». Методы для
# присвоения автомобилю года выпуска, типа и цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        self.launch = False

    def launch_engine(self):
        if not self.launch:
            print("Автомобиль заведён")
            self.launch = True

    def stop_engine(self):
        if self.launch:
            print("Автомобиль заглушен")
            self.launch = False

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year

my_car = Car("Red", "Roadster", 2024)

my_car.launch_engine()
my_car.stop_engine()
my_car.set_year(2024)
my_car.set_type("Coupe")
my_car.set_color("Blue")
my_car.launch_engine()


