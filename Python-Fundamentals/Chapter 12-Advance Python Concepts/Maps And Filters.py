# Map is used for applying a function to multiple items.
# Takes a list (or any sequence)
# Applies the same function to every item in that list
# Gives you back a new list (in Python 3, it gives a map object which you can convert to a list)
#
# Why use map?
# - It lets you transform each element in an iterable without writing an explicit loop.
# - It keeps code concise and easier to read when the same operation applies to every item.
# - It separates the transformation logic from the iteration logic.
# - In Python 3, map returns a lazy iterator, which can save memory when working with large data.
#
# When to use map?
# - Use map when you have a function and want to apply it to every element of an iterable.
# - Use map when the operation is simple and can be expressed in a single function call.
# - Use map when you want a functional-style alternative to a for-loop with append.
# - Avoid map if the operation is complex, needs side effects, or is easier to express with a simple loop.


a = [1,2,3,4,5]
# any iterable
result = map(lambda x : x*2, a)
# we need to convert the map object into a list to see the result
print(list(result))
# it is not necessary to use map with lambda; you can also use a named function but it is recommended
def double(x):
    return x*2
result2 = map(double,a)
print(list(result2))
# filters
# it filters out based on boolean expression 
# for suppose we r creating a function to check even number (note it works on lists)
# Filter as the name suggest is used to filter out the stuff.
# Takes a list (or other sequence)
# Checks each item using a function (a test)
# Keeps only the items that pass the test (i.e., return True)
def even(x):
    if x % 2==0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
result3 = filter(even,a)
print(list(result3))
# also this approach
result4 = filter(lambda x : True if x % 2 == 0 else False,a)
print(list(result4))