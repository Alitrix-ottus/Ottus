"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    ...

class NotEnoughFuel(Exception):
    ...

class CargoOverload(Exception):
    ...