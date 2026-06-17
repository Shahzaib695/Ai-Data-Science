class Animal:
    # types of attributes there are two types of attributes class and instance
    name = "Shahzaib" # this is a class attribute

    def __init__(self,age):
        self.age = age # this is an instance attribute

    # an instance emthod is a method which has self declared inside of its parameter because self clearly targets the location of an object or an instance so as soon as u write self inside of a function it becomes an isntance method 
    def instance_method(self):
        print("I am an insatnce method")
    # self targets object while cls targets class attribute and just like self.age we can only call cls.variable names which are present below the class like for this we have age
    @classmethod
    def class_method(cls):
        print("I am a class method")
    # a static method is just a simple function without any instance or class attribute
    @staticmethod
    def static_method():
        print("I am a static method")
obj = Animal(19)
obj.instance_method()
obj.class_method()
obj.static_method()