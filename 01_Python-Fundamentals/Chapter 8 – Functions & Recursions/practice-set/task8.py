# 8. Write a python function to print multiplication table of a given number.
n = int(input("Enter a number: "))
def multiplication(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}");
print(multiplication(n))