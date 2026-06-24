# To store data permenantly we use file option in python we can read write and do more operations on a file just in code for example i am creating a file named create.txt in which i am going to write something and we will read the content of that file here in code
f = open("create.txt")
# here u can see above i just have given the file name not the mode of it because by default open() mode is r 
data = f.read()
print(data)
f.close()
print('''File Modes In Python
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.''')