# from car import Car

# my_new_car = Car("Audi", "A4", 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Storing Multiple Classes in a Module
# You can store as many classes as you need in a single module, although each
# class in a module should be related somehow

# from car import ElectricCar

# my_leaf = ElectricCar("Nissan", "Leaf", 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# Importing Multiple Classes from a Moduel

# from car import Car, ElectricCar

# my_mustang = Car("Ford", "Mustang", 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar("Nissan", "Leaf", 2024)
# print(my_leaf.get_descriptive_name())

# Importing an Entire Module

import car

my_mustang = car.Car("Ford", "Mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar("Nissan", "Leaf", 2024)

# Import All Classes from a Module
# You can import all classes from a using the following syntax
# from module_name import *

# Importing a Module into a Module

