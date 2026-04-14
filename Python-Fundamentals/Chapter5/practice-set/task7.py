# If the names of 2 friends are same; what will happen to the program in problem 6?
# it will update the same name Because a dictionary cannot store duplicate keys.
# So when the same name is entered again, Python doesn’t create a second entry — it just replaces the old value with the new one for that key.
lang = {};
name1 = input("Enter Your Name: \n");
name2 = input("Enter Your Name: \n");
inp = input(f"Please Enter Your favorite language I Am talkin to {name1}:\n");
lang[name1] = inp;
inp1 = input(f"Please Enter Your favorite language I Am talkin to {name2}:\n");
lang[name2] = inp1;
print(lang)