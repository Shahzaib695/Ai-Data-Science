# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
dictionary = {
    "How Are You" : "Kese ho",
    "Help" : "Madad"
}
userInput = input("Enter a word to search in the dictionary");
if userInput in dictionary:
    print("Urdu Meaning: ",dictionary[userInput])
else:
    print("We Are SOrry As Our Data Is Limited Try Another Word")    