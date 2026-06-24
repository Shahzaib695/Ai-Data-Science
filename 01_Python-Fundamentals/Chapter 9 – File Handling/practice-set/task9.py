# Write a program to find out whether a file is identical & matches the content of another file.
with open("hiscore.txt") as h:
    verify = h.read()
with open("poems.txt") as p:
    verify2 = p.read()
if verify == verify2:
    print("Yes they are same")
else:
    print("Not Same")