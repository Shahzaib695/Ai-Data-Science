example = ["Apple","Banana",19,20,False];
print(example[0]);
# list in python are just like arrays i mean it can store any type of data in it 
example[0] = "Mango";
print(example[0]);
# its index is same like string start from 0 we can add remove things in lists as they are mutable
# unlike strings list can be changed 
print(example[0:3])
# unlike string it doesnot store in refernce memory it actually changes the whole list 
# for example when we use string function it only stores temporarly keeping th estring intact but in lists whole lists changes 

# adding a name in list
example.append("Shahzaib");
print(example); 
l1 = [10,21,45,67,908,87];
l1.sort()
print(l1);
l1.reverse();
print(l1);
l1.append(69);
print(l1);
l1.insert(3,8) #This will add 8 at 3 index.
print(l1)
l1.pop(2)   # Will delete element at index 2 and return its value.
print(l1)
l1.remove(21) # Will remove 21 from the list
print(l1)
# tuple is basically a list but its nature is mutable it will react similar to string
a = ("hello","hi", 187, 897, False);
print(type(a))
print(a[0]);
# tuple can be empty full it depends
# methods of tuples
val = a.count(187);
print(val);
ind = a.index(187);
print(ind);
# t = (1, 2, 3, 2, 2)
t = (1, 2, 3, 2, 4)
print(t.count(2))  # Output: 3
print(t.index(2))      # Output: 1
print(t.index(2, 2))   # Output: 3 (starts searching from index 2)
# t = (1, 2, 3)
print(len(t))  # Output: 3
# t = (1, 2, 3)
print(2 in t)      # True
print(4 not in t)  # True
# t = (1, 2, 3, 4, 5)
for item in t:
    print(item)

print(t[1:4])
# slicing