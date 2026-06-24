# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle
st = "twinkle"
with open("poems.txt",'w') as f:
    f.write(st)
with open("poems.txt","r") as f:
    content = f.read()
    print(content)
if st in content:
    print("True")
else:
    print("False")