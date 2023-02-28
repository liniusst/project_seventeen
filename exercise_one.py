# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.

class Calculator:

    def __init__(self, number_one: float, number_two: float) -> float:
        self.number_one: float = number_one
        self.number_two : float = number_two
        self.number_one = float(input("First number: "))
        self.number_two = float(input("Second one: "))

    def add(self):
        return self.number_one + self.number_two

    def sub(self):
        return self.number_one - self.number_two

    def muliply(self):
        return self.number_one * self.number_two

    def divide(self):
        return self.number_one / self.number_two 
    
calculation = Calculator(number_one= 5, number_two= 5)
print(calculation.add())
print(calculation.sub())
print(calculation.muliply())
print(calculation.divide())
