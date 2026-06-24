# Write a python program to find remainder when a number is divided by z.
a = int(input("Enter Number 1 To Divide: "));
b = int(input("Enter Number 2 So We Can Divide Number 1: "));
if b == 0:
    print("Number Not Valid");
    exit();
else:    
 c = a % b;
print(f"The reminder for {a} divided by {b} is {c}");