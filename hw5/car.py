"""
создайте класс `Car`, наследник `Vehicle`
"""

from .base import Vehicle
from .engine import Engine

class Car(Vehicle):
    def __init__(self, weight = 10, fuel = 40, fuel_consumption = 10.2):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine:Engine = None
    
    def set_engine(self, engine:Engine):
        if engine:
            self.engine = engine