class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Lays(Product):
    
    def __init__(self):
        super().__init__('Lays', 1.2)
        
class Coke(Product):
    
    def __init__(self):
        super().__init__('Coke', 0.4)
        
        