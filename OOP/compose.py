class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP starting...")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print(f"{self.model} car starting...")
        self.engine.start()

class Plane:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Plane has an Engine

    def start_plane(self):
        print(f"{self.model} plane starting...")
        self.engine.start()

# Creating an Engine object
engine = Engine(300)

# Creating a Car object with the Engine object
car = Car("Toyota", engine)
car.start_car()
# Output:
# Toyota car starting...
# Engine with 300 HP starting...

# Creating a Plane object with the same Engine object
plane = Plane("Boeing", engine)
plane.start_plane()
# Output:
# Boeing plane starting...
# Engine with 300 HP starting...
