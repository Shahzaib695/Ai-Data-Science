# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary = {
    "kese ho" : "How Are You",
    "Kiya" : "What",
    "Kese" : "How"
    }
userInput = input("Enter a word to search In the dictionary:\n");
# print(dictionary[userInput]);
if userInput in dictionary:
    print("English meaning:", dictionary[userInput]);
else:
    print("Not Found.");
