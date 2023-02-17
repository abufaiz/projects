#Project under Python Crash Course Chapter 9

''' Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open. Make an instance called restaurant from
your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, where we serve {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
# create an instance of the Restaurant class
restaurant = Restaurant("The Italian Kitchen", "Italian")

# print the restaurant name and cuisine type
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# call the describe_restaurant() and open_restaurant() methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


'''Create three different instances from the class, and call describe_restaurant() 
for each instance.'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
restaurant1 = Restaurant("Pizza Palace", "Italian")
restaurant2 = Restaurant("Curry Corner", "Indian")
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


'''Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user'''

class User:
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}year old {self.gender} who works as a {self.occupation}.")
        
    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back to our website!")

# Create three instances of the User class
user1 = User("Fatima", "Usman", 27, "female", "Data Analyst")
user2 = User("Adnan", "Muhammad", 30, "male", "Medical Doctor")
user3 = User("Hassan", "Adamu", 38, "male", "Lecturer")

# Call describe_user() and greet_user() for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

'''
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and 
print the value again. Add a method called increment_number_served() that 
lets you increment the number of customers who’ve been served. Call this method 
with any number you like that could represent how many customers were served in, 
say, a day of business.'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, increment):
        self.number_served += increment
        
    def customers_served(self):
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

restaurant = Restaurant("The Sizzling Sausage", "German")

# print the restaurant name and cuisine type
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# call the describe_restaurant() method
restaurant.describe_restaurant()

# call the open_restaurant() method
restaurant.open_restaurant()

# print the number of customers served
restaurant.customers_served()

# set the number of customers served to 50 and print the new value
restaurant.set_number_served(50)
restaurant.customers_served()

# increment the number of customers served by 10 and print the new value
restaurant.increment_number_served(10)
restaurant.customers_served()

'''Add an attribute called login_attempts to the User class. Write a method called 
increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of 
login_attempts to 0. Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User's name: {self.first_name} {self.last_name}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Hassan", "Adamu")
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")

'''An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. Create an instance of IceCreamStand, 
and call this method'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand and call the methods
my_ice_cream_stand = IceCreamStand("Scoops")
my_ice_cream_stand.flavors = ["chocolate", "vanilla", "strawberry"]
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()

'''An administrator is a special kind of user. Write a class called Admin 
that inherits from the User class Add an attribute, privileges, that stores 
a list of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s 
set of privileges. Create an instance of Admin, and call your method.'''

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Sani", "Adamu", 40, "Jigawa")
admin.describe_user()
admin.show_privileges()

'''

Write a separate Privileges class. The class should have one attribute, privileges, 
that stores a list of strings. Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges'''

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

admin = Admin("Sani", "Adamu", 40, "Jigawa")
admin.describe_user()
admin.show_privileges()


'''Battery Upgrade: Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 100 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery. You should 
see an increase in the car’s range'''

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.") 
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery.battery_size == 75:
            range = 260
        elif self.battery.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def upgrade_battery(self):
       if self.battery_size < 100:
           self.battery_size = 100


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.get_range()


'''Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance, 
and call one of Restaurant’s methods to show that the import statement 
is working properly import restaurant'''

import restaurant 

'''Start with your work from Exercise 9-8 (page 173). 
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges()
 to show that everything is working correctly. from user_admin import Admin'''

admin = Admin("Sani", "Adamu", 40, "Jigawa")
admin.describe_user()
admin.show_privileges()

'''Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create 
an Admin instance and call show_privileges() to show that everything is still 
working correctly'''


from admin import Admin

admin = Admin("Sani", "Adamu", 40, "Jigawa")
admin.describe_user()
admin.privileges.show_privileges()

'''Make a class Die with one attribute called sides, which has a default 
value of 6. Write a method called roll_die() that prints a random number 
between 1 and the number of sides the die has. Make a 6-sided die and roll it 
10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

# Create a 6-sided die and roll it 10 times
d6 = Die()
for i in range(10):
    d6.roll_die()

# Create a 10-sided die and roll it 10 times
d10 = Die(sides=10)
for i in range(10):
    d10.roll_die()

# Create a 20-sided die and roll it 10 times
d20 = Die(sides=20)
for i in range(10):
    d20.roll_die()

''': Make a list or tuple containing a series of 10 numbers and 
five letters. Randomly select four numbers or letters from the list and print a 
message saying that any ticket matching these four numbers or letters wins a 
prize'''

# define a list of 10 numbers and 5 letters
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
# randomly select four items from the list
winning_items = random.sample(my_list, 4)
# print a message announcing the winning items
print(f"Congratulations! Any ticket matching the following four items wins a prize: {winning_items}")


'''
 You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. Print a message 
reporting how many times the loop had to run to give you a winning ticket'''

# Define the pool of possible numbers and letters
pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [1, 2, 'A', 'B']

# Initialize a counter to keep track of how many times the loop runs
counter = 0

# Keep pulling numbers until your ticket wins
while True:
    # Randomly select four items from the pool
    winning_ticket = random.sample(pool, 4)
    
    # Check if the winning ticket matches your ticket
    if winning_ticket == my_ticket:
        print(f"Congratulations! You won the lottery after {counter} tries!")
        break
    
    # Increment the counter
    counter += 1

'''
: One excellent resource for exploring the 
Python standard library is a site called Python Module of the Week. Go to 
https://pymotw.com/ and look at the table of contents. Find a module that 
looks interesting to you and read about it, perhaps starting with the random
module.
Styling Classes
A few styling issues related to classes are worth clarifying, especially as your 
programs become more complicate'''
