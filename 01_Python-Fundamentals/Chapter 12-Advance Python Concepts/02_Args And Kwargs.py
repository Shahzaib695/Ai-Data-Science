# These are not special keywords the key thing is u can use any name just the main thing that should be done is using * and ** along with any name * so *args are used for multiple positional arguments, and **kwargs are used for multiple key word arguments * And the *args becomes a tuple and **kwargs becomes a dictionary
# now a situation u have a function with few variables as parameter which are responsible to store number than to process their addition for which we can use args and kwargs
def add(*args):
    sum = 0
    for i in args:
        sum = sum+i
    print (sum)
# now u can give 100 10 or ant arguments it will work smotthly
add(1,2,3,4,5,6)

# now lets see how to capture key and values a = "something"
def info(**info):
    print("Your Information Is As Follows")
    for i in info:
        print(f"{i} = {info[i]}")
info(Name = "Shahzaib",Age = 19, Designation = "Student")