class Car:
    '''Авто'''

    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

        print(f'New car: {self.name} (color {self.color}), police_car')

    def go(self, speed=30):
        self.speed = speed
        print(f'{self.name}: car is driving')

    def stop(self):
        self.speed = 0
        print(f'{self.name}: Car is stop')

    def turn(self,direction):
        print(f'{self.name}: Car is turn:')#{'right' if direction == 0 else left}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class CityCar(Car):
    '''City Car'''

#    def show_speed(self):
#        return f'{self.name}: Speed Car: {self.speed}. Speeding'
#            if self.speed > 60 else f'{self.name}: Speed: {self.speed}. Speeding'


class WorkCar(Car):
    '''Truck'''

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. Speeding'


class SportCar(Car):
    '''SportCar'''


class PoliceCar(Car):
    '''PoliceCar'''
    is_police = True


police_car = PoliceCar("Audi", "white", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Truck"', 'Black', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

sport_car = SportCar('"Truck"', 'Black', 40)
sport_car.go()
sport_car.turn(0)
print(SportCar.show_speed())
sport_car.turn(0)
sport_car.stop()

city_car = CityCar('"Truck"', 'Black', 40)
city_car.turn(1)
print(city_car.show_speed())
city_car.turn(0)
city_car.stop()

#print(f'{\nCar {city_car} (color {city_color.color})')
#print(f'{\nCar {police_car} (color {police_car.color})')
#add_commit