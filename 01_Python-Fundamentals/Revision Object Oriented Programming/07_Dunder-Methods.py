# Dunder methods are the one starting with __ and ending with __
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} how r u" #this will print this without calling the method directly
    def __add__(self, other):
        return f"The sum of both ages are {self.age + other.age}" 
        
obj = Animal("Lion",12)
obj2 = Animal("Tiger",14)
print(obj + obj2)