# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
print("Checking the file ..........................\n")
with open("task4.txt","r") as f:
    content = f.read();
if "Donkey" in content:
    print("Replacing The Word. Hang on its going to take a second")
    content = content.replace("Donkey","######")
    with open("task4.txt","w") as f:
        f.write(content)
    print("Phew! That was quick")
else:
    print("Didn't Found such word")