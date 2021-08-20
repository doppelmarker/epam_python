from collections import namedtuple

Car = namedtuple("Car", "color mileage")

car1 = Car("blue", 9999) or Car(color="red", mileage=5544)

car2 = Car("yellow", 9999) and Car(color="red", mileage=5544)

print(car1.color, car2.color)
