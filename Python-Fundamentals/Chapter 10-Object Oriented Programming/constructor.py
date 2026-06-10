# __ __ se start honw wale methods ko ham dunder methods kehte hai
# a constructor is automatically called when we are calling a class or when an object is created
class Employee:
    name = "Shahzaib"
    language = "Python"
    semester = "4th"
    def __init__(self,name,language,semester):
        print("Constructor Created")
        self.name = name
        self.language = language
        self.semester = semester
    def getInfo(self):
        print(f"The employee language is {self.language} and the employee semester is {self.semester}")
        # to add arguments from the class to a method inside of the class we use the built in keyword self
        # when we create a function that does not require anything from the class we call it as a static method 
    @staticmethod
    def greet():
        print("Hello! How Are You?")
# we can also create some thing like declaring different name and other things in a fucntion we can do this by using the same dunder method just we have to add the attributes as self.name and etc
Biodata = Employee("Shahzaib","PHP","6th")
Biodata.getInfo()
Biodata.greet()