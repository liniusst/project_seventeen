# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

class Employee:

    def __init__(self, name: str, surname: str) -> str:
        self.name: str = name
        self.surname: str = surname

    def merge_name_surname(self):
        return self.name + " " + self.surname
    
    def generate_email(self):
        return self.name.lower() + "." + self.surname.lower() + "@codeacademy.lt"

    
person_data = Employee(name= "Linas", surname= "Stonkus")
print(person_data.merge_name_surname())
print(person_data.generate_email())
        
