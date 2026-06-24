# Write a program to make a copy of a text file “this. txt”
with open("task6log.txt") as f:
    copy = f.read();
    
with open("task7.txt","w") as c:
    c = c.write(copy)
    