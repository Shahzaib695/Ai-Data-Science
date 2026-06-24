class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Coder(Programmer):
    c = 3
o = Employee()
print(o.a) #prints a value
# print(o.b) shows error
o = Programmer()
print(o.a,o.b) #we can now print o.b too as its now present in programmer class while o.a is inherited from employee class
o = Coder()
print(o.a,o.b,o.c) #now we can print it as its inherited from programmer and employee 