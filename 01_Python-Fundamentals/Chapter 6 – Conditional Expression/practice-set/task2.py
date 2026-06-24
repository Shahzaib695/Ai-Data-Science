# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
print('''
===============Pass Or Fail Checker==============      
''')
subject1 = int(input("Enter Subject 1 Marks \n"))
subject2 = int(input("Enter Subject 2 Marks \n"))
subject3 = int(input("Enter Subject 3 Marks \n"))
total = subject1+subject2+subject3
percentage = total/300*100
if(percentage >= 40):
    print("Pass");
else:
    print("Fail")