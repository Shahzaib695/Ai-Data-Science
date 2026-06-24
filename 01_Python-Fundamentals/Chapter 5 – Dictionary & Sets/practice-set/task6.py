# Create an empty dictionary. Allow 4 friends to enter their favorite language as  value and use key as their names. Assume that the names are unique.
lang = {}
for i in range (4):
    name = input("Enter Your Name: ");
    favourite_language = input(f"Hi {name}, what's your favorite language ")
    lang[name] = favourite_language;
print(lang)
