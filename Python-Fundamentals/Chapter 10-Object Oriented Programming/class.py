# A class is a blueprint for creating object.
class Employee:
    name = "Shahzaib"
    language = "Python"
    semester = "4th"

employee2 = Employee()
employee2.name = "Ali" # this is an instance attribute if it is not given it will return the default name written inside of the class 
print(employee2.name,employee2.language)
bioData = Employee()
print(bioData.language,bioData.semester)
# here name is an object attribute while other are class attribute as they belong to class there data is fetched from the class itself

print("A function present inside of the object or a class is a method.")