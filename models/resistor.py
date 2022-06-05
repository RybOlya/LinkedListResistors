class Resistor:

    def __init__(self, name: str, value: float, power: float, tolerance: float):
        self.name = name
        self.value = value
        self.power = power
        self.tolerance = tolerance

    def __str__(self):
        return f'Name: {self.name}, value: {self.value}, power: {self.power}, tolerance: {self.tolerance}'