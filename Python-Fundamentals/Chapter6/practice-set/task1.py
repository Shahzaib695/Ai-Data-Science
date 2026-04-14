#Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("Enter Num1:\n"))
num2 = int(input("Enter Num2:\n"))
num3 = int(input("Enter Num3:\n"))
num4 = int(input("Enter Num4:\n"))
if num1 > num2 and num1 > num3 and num1 > num4:
    greatest = num1;
elif num2 > num1 and num2 > num3 and num3 > num4:
    greatest = num2;
elif num3 > num1 and num3 > num2 and num3 > num4:
    greatest = num3;
else:
    greatest = num4;
print(f"Greatest Number is {greatest}");