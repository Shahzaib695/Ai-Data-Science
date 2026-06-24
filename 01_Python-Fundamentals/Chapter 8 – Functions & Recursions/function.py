# A Function is a group of statements performing a specific tasks its used to reduce redundancy and promotes code readability
# def avg():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = int(input("Enter a number: "))
#     average = (a+b+c)//3;
#     print(average)
# avg()    
# def greet():
#     name = input("Enter Your Name: ")
#     print(f"Assalamu Alaikum {name}")
# greet()
print("There are 2 types of Functions One is Built in functions and the other is User Defined Function")
# function with argument
# def greet(name):
#     print(f"Assalamu Alaikum {name}")
# greet("Shahzaib")
# return is used for returning a value to outside of the function
# there is also a thing known as default parameter like ke agar kisi ne koi name nahi dala we will assume the greet function i mean jese ek bande ne name nahi dala usne phir jake usse blank chordia so we can assign a default value like
def greet(name="Kuch Bhi"):
    print(f"Assalamu Alaikum {name}")
greet()