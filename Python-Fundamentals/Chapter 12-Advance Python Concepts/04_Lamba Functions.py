# Lamba is a function which helps to write a function in a single line
addition = lambda a,b : a+b
print(addition(1,2))
# we can also use if else but in ternary form
check = lambda a : "even" if a %2 == 0 else "odd"
print(check(24))