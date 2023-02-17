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