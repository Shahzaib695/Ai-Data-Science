class Employee:
    company = "Google"
    name = "Default"
    salary = "Default"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all language here is your language: {self.language}")

class Programmer(Employee,Coder):
    company = "Amazon"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()
print(a.company,b.company)
b.show()
b.printLanguage()
b.showLanguage()