#Repeat program 4 for a list of such words to be censored.
print("Checking for sensitive words in the file:..............................")
with open("task5.txt") as f:
    content  = f.read()
word = ["Donkey","Bag", "River", "Farmer", "Dog", "Barn", "Gate", "Stable", "Hay"]
for word in word:
    if word in content:
        print("Word detected sensoring it")
        content = content.replace(word,"#" * len(word))
    else:
        print("Not detected")
with open("task5.txt","w") as f:
    f.write(content)