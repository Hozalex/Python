import time
from functools import reduce


# 1
class TrafficLight:
    __color = None

    def running(self):
        while True:
            TrafficLight.__color = 'Red'
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'Yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'Green'
            print(TrafficLight.__color)
            time.sleep(5)


# light = TrafficLight()
# light.running()


# 2
print("2 _______________________")


class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        Road.__length = length
        Road.__width = width

    def weight(self):
        return (Road.__length * Road.__width * 25 * 5) // 1000


road = Road(20, 5000)
print(road.weight())

# 3
print("3 _______________________")


class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Position.name = name
        Position.surname = surname
        Position.position = position
        self._Worker__income['wage'] = wage
        self._Worker__income['bonus'] = bonus

    def get_full_name(self):
        return f'Full Name = {Position.name} {Position.surname}'

    def get_total_income(self):
        return f'Total income = {reduce(lambda x, y: x + y, (x for x in self._Worker__income.values()))}'


boss = Position('Ivan', 'Ivanov', 'boss', 100, 30)
print(boss.get_full_name())
print(boss.get_total_income())

# 4
print("4 _______________________")


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = None

    def go(self):
        print(f'{self.name} has go')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} has turned {direction}')

    def show_speed(self):
        print(f'your speed {self.speed}')


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        TownCar.name = name
        TownCar.color = color
        TownCar.speed = speed
        TownCar.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print('your speed is over limit 60')
        else:
            Car.show_speed(self)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        WorkCar.name = name
        WorkCar.color = color
        WorkCar.speed = speed
        WorkCar.is_police = is_police


def show_speed(self):
    if self.speed > 40:
        print('your speed is over limit 40')
    else:
        Car.show_speed(self)


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        SportCar.name = name
        SportCar.color = color
        SportCar.speed = speed
        SportCar.is_police = is_police


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        PoliceCar.name = name
        PoliceCar.color = color
        PoliceCar.speed = speed
        PoliceCar.is_police = is_police


work_car = WorkCar('work_lada', 'white', 50, False)
work_car.go()
work_car.show_speed()

town_car = TownCar('town_lada', 'green', 30, False)
town_car.go()
town_car.show_speed()
town_car.stop()

sport_car = SportCar('sport_lada', 'red', 80, False)
sport_car.go()
print(f'is this car police? {sport_car.is_police}')
sport_car.turn("left")
sport_car.show_speed()

police_car = PoliceCar('police', 'white-blue', 70, True)
police_car.go()
print(f'is this car police? {police_car.is_police}')
police_car.turn('right')
police_car.show_speed()
police_car.stop()
