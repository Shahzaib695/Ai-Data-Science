print("There Are Multiple way to represent a string which are as follows dont look at the output look at the code");
n1 = 'Shahzaib'; #single quotes 
n2 = "Shahzaib"; #double quotes
n3 = '''Shahzaib'''; #triple quotes its mostly used for multi line 
# String slicing
# Strings are immutable and we can slice it i mean ke specific part ko likh sakte hai like
n4 = len(n1); #To print length of the string
# The index starts from 0 from forwad when viewing it from reverse it starts from -1
print(n4); 
n5 = n1[0:3] # All the way from 0 to 2 exlcuding 3
print (n5);
n5 = n1[-4:-1] # All the way from -4 to -2 exlcuding -1
n6 = n1[4:7] # Same Output as above
print (n5);
print (n6);
# agar splice krte waqt [iske andar ye empty ho to iska matlab 0: or agar ye side empty ho to iska matlab length-1]
# skiping while splicing
# list[start : end : step]
# Where:
# start → index to begin at (inclusive)
# end → index to stop at (exclusive)
# step → how many indexes to skip each time
# yani iska matlab ye howa ke index 1-7 tk jao uske bad 3 step me 3 indexes ko skip kro yani 1-8 tk gaya uske bad usne 1 ko save rakha uske bad 2 index ko hataya yani 1,3 
sk1 = [1,2,3,4,5,6,7,8,9,10];
sk2 = sk1[1: 7 : 3];
print(sk2)
# 1. len () function – This function returns the length of the strings.
str = "harry"
print(len(str)) # Output: 5
# 2. String.endswith("rry") – This function_ tells whether the variable string ends with
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends
# with rry.
str = "harry"
print(str.endswith("rry")) # Output: True
# 3. string.count("c") – counts the total number of occurrences of any character.
str = "harry"
count = str.count("r")
print(count) # Output: 2
# 4. the first character of a given string.
str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"
# 5. string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string.
str = "harry"
index = str.find("rr")
print(index) # Output: 2
# 6. string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"
# escap sequence 
# \t => for tab space, \n => for new line, \' => for single quote ----> escape sequences there are others too which u can find after doing research.\
