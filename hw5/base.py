from abc import ABC
from exceptions import LowFuelError


class Vehicle(ABC):
    def __init__(self, weight:int=10, fuel:int=40, fuel_consumption:float=10.2):
        super().__init__()
        self.weight:int = weight
        self.started:bool = False
        self.fuel:int = fuel
        self.fuel_consumption:float = fuel_consumption
    
    def start(self):
        if not self.started:
            if not self.fuel:
                raise LowFuelError()
            
            self.started = True
    
    def move(self, distance:float):
        if self.fuel >= distance:
            self.fuel = self.fuel - distance
        else:
            raise LowFuelError()