# dictionary isse samjo just like assosiative array in php key value ke sath khel sakte
ages = {
    "Shahzaib" : 19,
    "Munawar" : 19,
    "Saim" : 19
}
print(ages);
print(type(ages));
print(ages["Saim"]);
#PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys

# methods of dictionary in python
a = {
    "name":"harry",
    "from":"india",
    "marks":[92,98,96]
    };
# a.items(): Returns a list of (key,value)tuples.
# a.keys(): Returns a list containing dictionary's keys.
# a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
# a.get("name"): Returns the value of the specified keys (and value is returned
# eg."harry" is returned here).
# More methods are available on docs.python.org
print(a.items())
print(a.keys())
a.update({"Harry" : 99, "Saim" : 100})
print(a);
print(a.get("Harry"))
# diff between get and normal method is that
# when we use get if the desired thing is not present it will return none and the normal one will return error breaking the code

# empty set is a dictionary which can be created by 
# s = {}
# its a dictionary to create an empty set we can use
d = set();
print(type(d));
s = {1,2,3,3,42,5,6,3,7,8,88,8,8, "Shahzaib"};
# a set always print a value once and that too not in order we can use strings also with it
#  we can also add elements in sets by using s.add
print(s)
s.add(69);
print(s)
print(type(s))
# more methods can be seen from chatGpt
# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values
# some methods of sets 
# len(s): Returns 4, the length of the set
# s.remove(8): Updates the set s and removes 8 from s.
# s.pop(): Removes an arbitrary element from the set and return the element
# removed.
# s.clear():empties the set s.
# s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
# s.intersection({8,11}): Return a set which contains only item in both sets {8}.
print(len(s));
s.remove(8);
print(s);
s1 = {1,2,3};
s2 = {3,4,5,6};
print(s1.union(s2))
print(s1.intersection(s2))