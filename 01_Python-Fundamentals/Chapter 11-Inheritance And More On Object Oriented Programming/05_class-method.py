# class Employee:
#     a = 1
#     def show(self):
#         print(f"The value of a in class attribute is {self.a}")
# e = Employee()
# e.a = 45
# e.show()
# this would show 45 because it will show instance value to tackle this we use class method so we could only show the value present in the class 
class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a in class attribute is {cls.a}")
e = Employee()
e.a = 45
e.show()
