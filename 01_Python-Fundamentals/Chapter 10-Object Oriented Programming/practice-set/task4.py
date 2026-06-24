# Add a static method in problem 2, to greet the user with hello.
# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of the given number is {self.n*self.n}")
    def cube(self):
        print(f"The cube of the given number is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root of the given number is {self.n**1/2}")
    @staticmethod
    def greet():
        print("Hello User")
number = Calculator(25)
number.greet()
number.square()
number.cube()
number.squareRoot()
