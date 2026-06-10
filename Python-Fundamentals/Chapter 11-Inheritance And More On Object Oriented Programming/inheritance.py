class Employee:
    company = "ITC"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
class Programmer(Employee):
    company = "ITC Infotech"
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language}")
a = Employee("Alice", 50000)
b = Programmer("Bob", 70000, "Python")
b.show()
b.showLanguage()
print(a.company, b.company)