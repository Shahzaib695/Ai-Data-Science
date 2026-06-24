f = open("create.txt")
print(f.read())
f.close()

# this same can also be done using 
with open("myfile.txt") as f:
    print(f.read())
