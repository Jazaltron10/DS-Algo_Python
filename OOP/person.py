class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, {self.age} years old")

    def __del__(self):
        print(f"Person deleted: {self.name}")

# Create an object of Person class
person = Person("John", 30)

# Deleting the person object to see the destructor message
del person
