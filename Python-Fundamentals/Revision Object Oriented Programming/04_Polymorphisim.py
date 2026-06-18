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