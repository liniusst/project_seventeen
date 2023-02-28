# Object-oriented programming (OOP)
from datetime import date

class Person:
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname

    def greet(self):
        return f"Hello, my name is {self.name}"
    
    def walk_away(self):
        return f"{self.name} is walking away.."
    
    def black_friday(self) -> int:
        deadline = date(2023, 11, 24)
        today = date.today()
        delta = deadline - today
        return delta.days
    
    def get_eye_color(slef, eye_color: str = "Brown") -> str:
        return eye_color

        

person = Person(name= "Linas", surname= "Stonkus")

# print(person.greet())
# print(person.walk_away())
# print(person.black_friday())
print(person.get_eye_color())
