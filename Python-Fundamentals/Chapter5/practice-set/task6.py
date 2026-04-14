# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
lang = {};
name1 = input("Enter Your Name: \n");
name2 = input("Enter Your Name: \n");
name3 = input("Enter Your Name: \n");
name4 = input("Enter Your Name: \n");
inp = input(f"Please Enter Your favorite language I Am talkin to {name1}:\n");
lang[name1] = inp;
inp1 = input(f"Please Enter Your favorite language I Am talkin to {name2}:\n");
lang[name2] = inp1;
inp2 = input(f"Please Enter Your favorite language I Am talkin to {name3}:\n");
lang[name3] = inp2;
inp3 = input(f"Please Enter Your favorite language I Am talkin to {name4}:\n");
lang[name4] = inp3;
print(lang)