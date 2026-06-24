# Write a program using functions to find greatest of three numbers.
a = 190
b = 90
c = 100

def greatest(a,b,c):
    if (a>b and a>c):
        return f"The greatest number is {a}"
    elif (b>a and b>c):
        return f"The greatest number is {b}"
    else:
        return f"The greatest number is {c}"
result = print(greatest(a,b,c))
