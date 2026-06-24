# A decorator is just a function that modifies another function without changing its actual code.
# lets look at example
def decorate(func):
    def wrapper():
        print("I will print myself before the function")
        func()
        print("I will print after the function executes")
    return wrapper

@decorate
def hello():
    print("hello i am shahzaib")

hello()

# lets suppose now we have a function with two parameters so the decorator function for that would be like

def decorater(func):
    def wrapper(a,b):
        print("Addition of the given numbers are as follows")
        func(a,b)
        print("I hope u liked this")
    return wrapper

@decorater
def add(a,b):
    print(a+b)
add(1,2)
# but the twist comes when u dont know how many arguments could be given to your function it could be 2 or 3 or 30 this will also force u to change your parameters in the decorator function to tackle that issue we have a thing called *args and *kwargs we have covered this topic in the next file
