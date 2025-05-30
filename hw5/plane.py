"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, max_cargo:int, weight = 10, fuel = 40, fuel_consumption = 10.2):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo:int
        self.max_cargo:int = max_cargo
    
    def load_cargo(self, number:int):
        if (self.cargo + number) > self.max_cargo:
            raise CargoOverload()
    
    def remove_all_cargo(self):
        tmp_cargo = self.cargo
        self.cargo = 0
        
        return tmp_cargo