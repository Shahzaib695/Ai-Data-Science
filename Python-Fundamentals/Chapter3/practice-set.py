# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter Your Name For A Surpurise \n");
gender = input("Enter Your Gender ").strip().lower();
# .strip() removes spaces while .lower() converts the string into lower case
if gender == "male":
    pronoun = "Mr" 
elif gender == "female":
    pronoun = "Ms"
else:
    print("Invalid Input");
    exit();        
print("Good Afternoon" , pronoun , name );
# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
day = int(input("Enter The Day (1-31)\n"));
if day < 1 or day > 31:
    print("Invalid day");
    exit();
month = int(input("Enter The Month (1-12) \n"));
if month < 1 or month > 12:
    print("Invalid month");
    exit();
year = int(input("Enter Year \n"));
date = f"{day:02d}/{month:02d}/{year}";
letter = letter.replace("<|Name|>", f"{pronoun} {name}");
letter = letter.replace("<|Date|>", date);
print(letter);
# f is for template literal 02d means if there is a single digit add 0 before it and 2 means to make it visible as 2 digits d means decimal
# .replace replaced that required string with the new variables
# Write a program to detect double space in a string.
text = input("Enter a string: ");
if "  " in text:
    print("Double space detected! ");
else:
    print("No Space Detected");
# Write a program to detect double space in a string.
text2 = input("Enter a string: ");
if " " in text:
    print("Single space detected! ");
else:
    print("No Space Detected");
# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!'
letter2 = "Dear Harry,\nThis python course is nice.\n Thanks!"
print(letter2);
