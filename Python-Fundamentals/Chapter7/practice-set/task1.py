# 1. Write a program to print multiplication table of a given number using for loop
number = int(input("Enter a number: "));
for i in range(0,11):
    print(f"{number} * {i} = {number * i}");

