""" the task 1 """
import time

class TrafficLight:
    __color = ['\033[41m', '\033[43m', '\033[42m', '\033[43m']

    def running(self):
        i = 0
        j = 0
        while True:
            print(f"{self.__color[i]}   \033[0m", end="\r")
            i += 1
            if i >= len(self.__color):
                i = 0

            if j == 0:
                time.sleep(7)
                j +=1
            elif j == 1:
                time.sleep(2)
                j = 0

a = TrafficLight()
a.running()


""" the task 2 """
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        print(f"Вес асфальта равен: {(self._length * self._width * 25 * 5) / 1000}")

a = Road(20, 5000)
a.calc()


""" the task 3 """
class Worker():

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def __init__(self,name, surname, position, wage, bonus):
        super().__init__(name, surname, position, {"wage": wage, "bonus": bonus})

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

a = Position("Vasya", "Krupenya", "Manager", 10000, 1000)
print(f"Full name: {a.get_full_name()}")
print(f"Income: {a.get_total_income()}")


""" the task 4 """
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} едет вперед")

    def stop(self):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} остановился")

    def turn(self, direction):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Скорость атвомобиля {self.name}: {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Автомобиль {self.name} Превысел скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    pass

car_1 = TownCar(59, 'white', 'TownCar', False)
car_1.go()
car_1.turn("налево")
car_1.show_speed()
car_1.stop()
print()
car_2 = SportCar(90, 'red', 'SportCar', False)
car_2.go()
car_2.turn("чуть налево")
car_2.show_speed()
car_2.stop()
print()
car_3 = WorkCar(50, 'yellow', 'WorkCar', False)
car_3.go()
car_3.turn("направо")
car_3.show_speed()
car_3.stop()
print()
car_4 = PoliceCar(170, 'blue', 'PoliceCar', True)
car_4.go()
car_4.turn("чуть правее")
car_4.show_speed()
car_4.stop()


""" the task 5 """
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск программы")


class Pen(Stationery):
    def draw(self):
        print(f"Что бы написать мой номер, нужна {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Для рисования, возьмем {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Разукрасим с помощью {self.title}а")


pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()