class Student:
    name = "Shahzaib" #variables defined inside the class are known as attributes
    def hello(self): #functions declared inside of the class are known as methods
        print("How are you ?")
    print("Hello i am being intialized")
# whenever we write a class it runs for a single time by default
# for suppose we call the variable name from Student class but it will just give an error because its declared inside the class scope as its not in global scope so to tackle this what we can do is we can call it simply by using two ways
a = Student() # its an object it has all the powers of class
print(a.name)
# or
print(Student.name)
a.hello()
# a constructor is used because we cant give parameters to a class for which reasons constructors are used
class Factory:
    # its a constructor
    # the word self captures the memory location of an object and for parameters it saves the value for the parameter that its taregting i hope u got my point
    def __init__(self,material,pockets,zips):
        self.material = material #its targeting the object and saving the value which will be given in the parameter u can notice how its colour changed
        self.pockets = pockets
        self.zips = zips
    def show(self):
        print(f'''Your object details are as follows:
Material -> {self.material}
Pockets -> {self.pockets}
Zips -> {self.zips}''')
Nike = Factory("Jersey",2,3)
# we can individually print everything seprately like
print(Nike.material)
Nike.show()


        