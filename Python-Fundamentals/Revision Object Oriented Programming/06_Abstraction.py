# Python doesnt support abstraction we can do it using an external library 
from abc import ABC, abstractmethod
# to understand the concept of abstraction lets take an example of something like resturant u have seen many franchises of resturant yet they follow the same recipe same style same uniform same theme and much more which are common among each other. I have given this example becuase they follow some rules which are same all around the franchises here comes abstraction which is a set of rules declared at the start which all classes have to follow. Here we are taking example of circle and square in the example to calculate there area
class abstract(ABC):
    @abstractmethod #this highlights abstract method
    def area(self):
        pass
class Square(abstract):
    def __init__(self,sides):
        self.sides = sides
class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        pass
obj = Circle(12)
# if we run these we would encounter error which u can check too i have attached the screenshot of the error that is coming without adding the implementation. Now no error is coming after we have added the implementation
