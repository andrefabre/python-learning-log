#-------------------------------------------------------------------------------
#   Chapter 9: Classes
#-------------------------------------------------------------------------------

# Object Orientated Programming is one of the most effective approaches to 
# writing software. In object orientated programming you write classes that
# represent real-world things and situations, and you create objects based on
# these classes. When you write a class you define the general behaviour that a
# whole category of objects can have

# Making an object from a class is called 'instantiation', and you work with
# instances of a class, and create instances of that class.
# Every method call associated with an instance automatically passes 'self',
# which is a reference to the instance itself; it gives the individual instance
# access to the attributes and methods in the class..
# Any variable prefixed with self is available to every method in the class, and
# we'll be able to access these variables through any instance created from the
# class.

# Creating and Using a class

class Dog (object):
    """Initialise name and age attributes"""
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# Making an instance from a class

my_dog = Dog("Willie", 12)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years of age.")

# Accessing attributes
# To access attributes of an instance, we use dot notation

# Calling methods
# To call a method, give the name of the instance and the method you want to
# call

my_dog.roll_over()
my_dog.sit()

# Creating multiple instances
# You can create as many instances as you need

your_dog = Dog("Axl", 4)
my_dog = Dog("Willie", 12)

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.1 Restaurant: Make a class called Restaurant. The __init__ method for
#   Restaurant should store two attributes: a restaurant_name and a
#   cuisine_type. Make a method called describe_restaurant() that prints these
#   two pieces of information, and a method called open_restaurant() that prints
#   a message indicating that the restaurant is open.
#-------------------------------------------------------------------------------

class Restaurant(object):
    """Initialise name and cuisine type attributes"""
    
    def __init__(self, restaurant_name, cuisine_type):
        
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        return(f"Restaurant Name: {self.name} Cuisine: {self.cuisine}")
        
    def open_restaurant(self):
        return(f"The {self.name} is now open for business")
        
my_restaurant = Restaurant("Charlie's", "Italian")
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.2 Three Restaurant: Start with your class from Ex 9.1. Create three
#   different instances from the class, and call describe.restaurant() for each
#   instance
#-------------------------------------------------------------------------------

restaurant_0 = Restaurant("John's", "Italian")
restaurant_1 = Restaurant("Holly", "Asian")
restaurant_2 = Restaurant("Alex", "Chinese")

print(restaurant_0.describe_restaurant())
print(restaurant_1.describe_restaurant())
print(restaurant_2.describe_restaurant())

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.3 Make a class called User. Create two attributes called first_name
#   and last name, and then create several other attributes that are typically
#   in a user profile. Make a method called describe_user() that prints a
#   summary of the user's information. Make another method called greet_user()
#   that prints a personalised greeting to the user.
#   Create several instances representing different users, and call both methods
#   for each user
#-------------------------------------------------------------------------------

class User(object):
    
    def __init__(self, user_name, first_name, last_name, email, age, role):
        
        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.role = role
    
    def describe(self):
        """Returns a description of the user profile."""
        return (f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail Address: {self.email}\nAge: {self.age}\nRole: {self.role}")
    
    def greet_user(self):
        """Returns a greeting to the user"""
        return(f"Hello, {self.first_name} {self.last_name}")
    

User_0 = User("TheDarkness", "Andre", "Fabre", "TheDarkness@google.com", 22, "Project Manager")
User_1 = User("BornAgainChristian", "Steve", "McDally", "BornAgainChristian@gmail.com", 34, "Business Analyst")
User_2 = User("BigPoppa", "Destiny", "Duke", "DestinyDuke@gmail.com", 18, "Project Administrator")

print(User_0.greet_user())
print(User_0.describe())
print(User_1.greet_user())
print(User_1.describe())
print(User_2.greet_user())
print(User_2.describe())

#-------------------------------------------------------------------------------
# Working with Classes and Instances
# You can modify the attributes of an instance directly or write methods that
# update attributes in specific ways

# Setting a Default Value of an Attribute
# When an instance is created, attributes can be defined without being passed in
# as parameters. These attributes can be define in the __init__() method, where
# they are assigned a default value.

class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values
# You can change an attribute's value in three ways
#   1. Directly through an instance
#   2. Set the value through a method
#   3. Increment the value through a method

# Modifying an Attribute's value directly

my_new_car.odometer_reading = 44
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
# Instead of accessing the attribute directly, you pass the new value to a 
# method that handles the updating internally

my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.update_odometer(10)

# Incrementing an Attribute's Value through a method

my_used_car = Car("Subaru", "Outback", 1990)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.4 Start with your program from Ex 9.1. Add an attribute called 
#   number_served with a default value of 0. Create an instance called
#   restaurant from this class. Print the number of customers the restaurant
#   has served, and then change this value and print again.
#-------------------------------------------------------------------------------

class Restaurant(object):
    """Initialise name and cuisine type attributes"""
    
    def __init__(self, restaurant_name, cuisine_type):
        
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        return(f"Restaurant Name: {self.name} Cuisine: {self.cuisine}")
        
    def open_restaurant(self):
        return(f"The {self.name} is now open for business")
    
    def guests_served(self):
        return(f"You have served {self.number_served} guests.")
    
    def set_number_served(self, guest_amount):
        self.number_served = guest_amount
    
    def increment_number_served(self, guest_count):
        self.number_served += guest_count
    
new_restaurant = Restaurant("Biggies", "Dirty South")
print(new_restaurant.guests_served())

new_restaurant.number_served = 20
print(new_restaurant.guests_served())

new_restaurant.set_number_served(15)
print(new_restaurant.guests_served())

new_restaurant.increment_number_served(10)
print(new_restaurant.guests_served())

#-------------------------------------------------------------------------------

# Inheritance
# If the class you are writing is a specialised version of another class you
# wrote, you can use inheritance
# When one class inherits from another, it takes on the attributes and methods
# of the first class.
# The original class is called the parent class, and the new class is the
# child class

# The __init__ Method for a Child Class
# When you're writing a new class based on an existing class, you'll often want 
# to call the __init__() method from the parent class. This will initialise
# any attributes that were defined in the parent __init__() method and them
# available in the child class

# When you create a child class, the parent class must be part of the current
# file and must appear before the child class in the file

# class ElectricCar(Car):
#     """"Represents aspects of a car, specific to electric vehicles."""
    
#     def __init__(self, make, model, year):
#         """Initialise attributes of the parent class"""
#         super().__init__(make, model, year)
#         self.battery_size = 40
    
#     def describe_battery(self):
#         """Print a statement describing the battery size"""
#         return(f"This car has a {self.battery_size}--kWh battery.")
        
# my_leaf = ElectricCar("Nissan", "Leaf", 1990)
# print(my_leaf.get_descriptive_name())
# print(my_leaf.describe_battery())

# Defining Attributes and Methods for the Child Class

# Instances as Attributes
class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """"Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialise attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
        
my_leaf = ElectricCar("Nissan", "Leaf", 1990)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.6 Ice Cream Stand: An icecream stand is a specific kind of restaurant.
#   Write a class called IceCreamStand that inherits from the Restaurant class
#   you wrote in Ex 9.1 or 9.4. Add an attribute called flavours that stores a
#   list of icecream flavours. Write a method that displays these flavours.
#   Create an instance of IceCreamStand, and call this method
#-------------------------------------------------------------------------------

class Restaurant(object):
    """Initialise name and cuisine type attributes"""
    
    def __init__(self, restaurant_name, cuisine_type):
        
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        return(f"Restaurant Name: {self.name} Cuisine: {self.cuisine}")
        
    def open_restaurant(self):
        return(f"The {self.name} is now open for business")
    
    def guests_served(self):
        return(f"You have served {self.number_served} guests.")
    
    def set_number_served(self, guest_amount):
        self.number_served = guest_amount
    
    def increment_number_served(self, guest_count):
        self.number_served += guest_count

class IceCreamStand(Restaurant):
    """A specific kind of Restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of the class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["Vanilla", "Chocolate", "Strawberry"]
        
    def display_flavours(self):
        return (f"Here is our list of flavours {self.flavours}")
    
new_restaurant = Restaurant("Biggies", "Dirty South")
print(new_restaurant.guests_served())

new_restaurant.set_number_served(20)
print(new_restaurant.guests_served())

new_icecream_stand = IceCreamStand("Gelato", "All you can eat")
print(new_icecream_stand.display_flavours())

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.7 Admin: An administrator is a special kind of user. Write a class called
#   Admin that inherits from the User class you wrote in Ex 9.3 or Ex 9.5
#   Add an attribute, privileges, that stores a list of strings like
#   "can add post", "can delete post", "can ban user", and so on.
#   Write a method called show_privileges() that lists the administrator's set
#   of privileges. Create an instance of Admin, and call your method
#-------------------------------------------------------------------------------

class User(object):
    
    def __init__(self, user_name, first_name, last_name, email, age, role):
        
        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.role = role
    
    def describe(self):
        """Returns a description of the user profile."""
        return (f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail Address: {self.email}\nAge: {self.age}\nRole: {self.role}")
    
    def greet_user(self):
        """Returns a greeting to the user"""
        return(f"Hello, {self.first_name} {self.last_name}")
    
class Administrator(User):
    """Inherits from class User"""
    
    def __init__(self, user_name, first_name, last_name, email, age, role):
        super().__init__(user_name, first_name, last_name, email, age, role)
        self.privileges = ["Create User", "Update User", "Delete User"]
    
    def show_privileges(self):
        return (f"Admin privileges: {self.privileges}")
    
    
admin_user = Administrator("The Darkness", "Andre", "Fabre", "TheDarkess@google.com", 22, "Administrator")
print(admin_user.describe())
print(admin_user.show_privileges())

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.8 Privileges: Write a separate Privilegs class. The class should have one
#   attribute, privileges, that stores a list of strings as described in Ex. 9.7
#   Make a privileges instance as an attribute in the Admin class. Create a new
#   instance of Admin and user your method to show its privileges
#-------------------------------------------------------------------------------

class User(object):
    
    def __init__(self, user_name, first_name, last_name, email, age, role):
        
        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.role = role
    
    def describe(self):
        """Returns a description of the user profile."""
        return (f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail Address: {self.email}\nAge: {self.age}\nRole: {self.role}")
    
    def greet_user(self):
        """Returns a greeting to the user"""
        return(f"Hello, {self.first_name} {self.last_name}")

class Privileges(object):
    """Displays user privileges"""
    
    def __init__(self):
        self.privileges = ["Create User", "Update User", "Delete User"]
    
    def show_privileges(self):
        return (f"Admin privileges: {self.privileges}")
    
class Administrator(User):
    """Inherits from class User"""
    
    def __init__(self, user_name, first_name, last_name, email, age, role):
        super().__init__(user_name, first_name, last_name, email, age, role)
        self.privileges = Privileges()
    

    
admin_user = Administrator("The Darkness", "Andre", "Fabre", "TheDarkess@google.com", 22, "Administrator")
print(admin_user.describe())
print(admin_user.privileges.show_privileges())

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   9.9 Battery Upgrade: Use the final version of electric_car.py from this
#   section. Add a method to the Battery class called upgrade_battery(). This
#   method should check the battery size and set the capacity to 65 if it isn't
#   already. Make an electric car with a default battery size, call get_range()
#   once, and then call get_range a second time after upgrading the battery. 
#   You should see an increase in the car's range.
#-------------------------------------------------------------------------------

class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """"Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialise attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def upgrade_battery(self):
        if self.battery.battery_size != 65:
            self.battery.battery_size = 65
        
my_leaf = ElectricCar("Nissan", "Leaf", 1990)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.upgrade_battery()
my_leaf.battery.get_range()

#-------------------------------------------------------------------------------

# The Python Standard Library

from random import randint
