# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
grade = float(input("Enter Your Percentage:\n"));
if(grade >= 90 ):
    print("EX");
elif(grade >= 80):
    print("A");
elif(grade >= 70):
    print("B");
elif(grade >= 60):
    print('C');
elif(grade >= 50):
    print('D');
else:
    print("F");
