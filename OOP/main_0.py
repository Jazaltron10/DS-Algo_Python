# import sys
# sys.path.append('C:/Users/Jasper Albert Nri/PycharmProjects/DS_and_Algo')
from OOP.car import Car
from OOP.product import Product
from OOP.student import Student


# Creating an Instance of the car class 
vehicle_1 = Car("Toyota", "Camry", 1998)
print(vehicle_1.get_descriptive_name())

my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descriptive_name())  # Output: 2020 Toyota Camry

my_car.read_odometer()  # Output: This car has 0 miles on it.
my_car.update_odometer(100)  # Update odometer reading
my_car.read_odometer()  # Output: This car has 100 miles on it.

my_car.increment_odometer(50)  # Increment odometer reading
my_car.read_odometer()  # Output: This car has 150 miles on it.



# NOW FOR THE STUDENT CLASS 
student1 = Student("Alice", 21)
student1.display_student_info()


# NOW FOR THE PRODUCT CLASS 
product1 = Product("Laptop", 1000, 5)
print(f"\nTotal Value ${product1.calculate_total_value()} ")