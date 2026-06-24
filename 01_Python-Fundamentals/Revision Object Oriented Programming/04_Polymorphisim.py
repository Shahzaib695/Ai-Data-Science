# method overriding
class Intro:
    def show(self):
        print("Hello how r u")
class Intro2(Intro):
    def show(self):
        print("Hi hello")
obj = Intro2()
obj.show()
# this will override the intro show() method and will use the intro2 show method and if u access intro1 class u will be shown the first method this is simple method overloading
# method overloading is not supported in python :( 
# Write your code here for Q15
# by default python doesnt support overloading but we can do it using *args which converts it into a tuple and deal with arguments
class Calculator:
    def add(self,*args):
        return sum(args)
obj = Calculator()
print(obj.add(5))
print(obj.add(5,100))
print(obj.add(5,89,90))
# there is a concept of duck typing in python which in short does this
class Animal:
    def show(self):
        print("Hello")
class Human:
    def show(self):
        print("Hello too")
obj = Animal()
obj2 = Human()
obj.show()
obj2.show()
# same method but called from different class shows different result