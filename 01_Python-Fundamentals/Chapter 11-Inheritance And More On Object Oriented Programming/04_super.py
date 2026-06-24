# for suppose ham sab ka constructor banate hai har class ka jo class call krege sirif usi ka constructor call hoga baqio ka nahi to if hame inherited class ka constructor call krna howa to we use super lets see below
class Employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
# lets call the cosntructor of programmer
class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")
    c = 3
o = Employee()
print(o.a) #prints a value
# print(o.b) shows error
o = Programmer()
print(o.a,o.b) #we can now print o.b too as its now present in programmer class while o.a is inherited from employee class
o = Coder()
print(o.a,o.b,o.c) #now we can print it as its inherited from programmer and employee 