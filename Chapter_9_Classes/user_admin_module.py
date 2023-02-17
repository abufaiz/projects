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

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()