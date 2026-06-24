# Write a program to wipe out the content of a file using python.
with open("sample.txt","w") as f:
    delete = f.write("")
    print("Done")