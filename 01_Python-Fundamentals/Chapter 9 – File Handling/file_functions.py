# here we are going to be using readlines function which reads line by line what is written in the files now we are going to do is create a file and add few lines in it or we can use the previous files too keep in mind this function returns functions in form of list
f = open("create.txt")
# lines = f.readlines()
# we can also use readline function to print a single line of our choice this function returns the lines inform of strings
line = f.readline()
# print(line,type(line))

# print(lines,type(lines))
# lets print line using while loop not lines i am talking about each line seprately using readline function
# easy
while (line != ""):
    print(line)
    line = f.readline()
f.close()