class Product:
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity 
        
    def calculate_total_value(self):
        total_value = self.price * self.quantity
        return total_value