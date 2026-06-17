# inheritance 
# for it we are creating a parent class/super class or a child class/sub class
class FactoryKhi:
    a = "We are present all around Pakistan"
    def show(self):
        print("I am an instance method inside of factory")
# lets see how inheritance works
class FactoryLhr(FactoryKhi):
    pass
# now this method can access all the things insdie of the main class
# obj = FactoryLhr()
# print(obj.a)
# obj.show()
# when we inherit a class we not only get any methods only we get all the instances of the class too
class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Your name is {self.name}")
class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
# now main issue is that the show function is basically present in the animal class and its not printing age of the human so to avoid that we will be creating a new show function with the addition of self.age
    def show(self):
        print(f"Your name is {self.name} and age is {self.age}")
obj = Human("Shahzaib",19)
obj.show()
# for example when u want to ask age of human but not disturbing the inheritance situation we can do it by using the super keyword

# multiple inheritance lets see
class Example1:
    name1 = "Example1"
class Example2:
    name2 = "Example2"
class Example3(Example1,Example2):
    name3 = "Example3"
obj = Example3()
print(obj.name1 ,obj.name2 ,obj.name3);
# when inheriting the constructor function will be called of the first inherited class like for this Example1 constructor would be called 

class MainFactory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
class KhiFactory(MainFactory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
class LhrFactory(KhiFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
mat = LhrFactory("Silk",2,"Black",3)
print(mat)