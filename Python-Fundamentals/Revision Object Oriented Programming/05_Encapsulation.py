# encapsulation basic defination is like restricting access inshort public private game
# public thing as we saw in our previous code how an object can access the class's everything sometimes we have to change access like restricting access to a specific thing like account balance or something like that i hope u got my point this is where encapsulation enters the chat
# now for example purpose i am doing a normal example
# class Factory:
#     a = "Karachi"
#     def show(self):
#         print("Hello We are located in karachi")
# class Factory2(Factory):
#     b = "Lahore"
#     def show2(self):
#         print(super().a)
# obj = Factory2()
# obj.show2()
# here u can see i can print any method from the inherited class and even its variable
# python doesnt support private thing :( so for naming convention we use this approach to tell the developers its a protected thing
class Factory:
    # we just add _ to show it is protected
    _a = "Karachi"
    def _show(self):
        print("Hello We are located in karachi")
class Factory2(Factory):
    b = "Lahore"
    def show2(self):
        print(super()._a)
obj = Factory2()
obj.show2()

# now a twist that u might not thought would happen so here we go we can actually make private attributes and methods by using two underscores __ lets see the example
class Factory3:
    __a = "Karachi"
    def show(self):
        print("Hello We are located in karachi")
class Factory4(Factory3):
    b = "Lahore"
    def __show2(self):
        print(super().__a)
obj2 = Factory4()
obj2.__show2()
# see now its private

# separate example demonstrating encapsulation with a student record
class StudentRecord:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def update_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

    def get_grade(self):
        return self.__grade

student = StudentRecord("Sara", 88)
print(student.name, student.get_grade())
student.update_grade(92)
print("Updated grade:", student.get_grade())
# direct access to student.__grade is not allowed from outside the class
