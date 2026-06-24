# to create an empty set we dont use s = {} instead we use s = set() this creates an empty set
e = set();
print(type(e))
# it does not add duplicate data 
s = {1,2,3,3,3,4,5,6,6,6,"Shahzaib",1.099}
print(s)
# we can store any type of data in sets
print('''PROPERTIES OF SETS
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.''')