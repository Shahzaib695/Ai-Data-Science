# in this file we will be creating a file named myfile and it will automatically create it in the folder
st = "Hello! We are checking python built in functions"
f = open("myfile.txt",'w')
# here w means write
f.write(st)
f.close()