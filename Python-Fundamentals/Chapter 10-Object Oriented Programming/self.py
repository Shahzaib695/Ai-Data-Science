class Employee:
    name = "Shahzaib"
    language = "Python"
    semester = "4th"
    
    def getInfo(self):
        print(f"The employee language is {self.language} and the employee semester is {self.semester}")
        # to add arguments from the class to a method inside of the class we use the built in keyword self
        # when we create a function that does not require anything from the class we call it as a static method 
    @staticmethod
    def greet():
        print("Hello! How Are You?")
Biodata = Employee()
Biodata.getInfo()
Biodata.greet()