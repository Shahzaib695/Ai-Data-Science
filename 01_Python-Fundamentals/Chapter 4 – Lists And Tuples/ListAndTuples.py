example = ["Apple","Banana",19,20,False];
print(example[0]);
# list in python are just like arrays i mean it can store any type of data in it 
example[0] = "Mango";
print(example[0]);
# its index is same like string start from 0 we can add remove things in lists as they are mutable unlike strings list can be changed 
print(example[0:3])
# unlike string it doesnot store in refernce memory it actually changes the whole list 
# for example when we use string function it only stores temporarly keeping the string intact but in lists whole lists changes 
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
# insert(index, eleemnt) is used to insert an element at a specific index in the list. It takes two arguments: the index where you want to insert the element and the element itself.
l1.insert(3,8) #This will add 8 at 3 index.
print(l1)
l1.pop(2)   # Will delete element at index 2 and return its value.
print(l1)
# difference between pop and remove is that pop will return the value of the element it removed while remove will not return anything it just removes the element from the list
l1.remove(21) # Will remove 21 from the list
print(l1)
# tuple is basically a list but its nature is mutable it will react similar to string
a = ("hello","hi", 187, 897, False);
print(type(a))
print(a[0]);
# tuple can be empty full it depends
# methods of tuples
print("Count function in tuple. It counts how many times a specific element appears in the tuple.");
val = a.count(187);
print(val);
print("Index function in tuple. It returns the index of the first occurrence of a specific element in the tuple.");
ind = a.index(187);
print(ind);
# t = (1, 2, 3, 2, 2)
t = (1, 2, 3, 2, 4)
print(t.count(2))  # Output: 3
print(t.index(2))      # Output: 1
# t.index(2, 2) will start searching for the element 2 from index 2 onwards. It will return the index of the first occurrence of 2 after index 2.
print(t.index(2, 2))   # Output: 3 (starts searching from index 2)
# t = (1, 2, 3)
print(len(t))  # Output: 3
# t = (1, 2, 3)
# 2 in t will check if the element 2 is present in the tuple t. It will return True if 2 is found in the tuple, and False otherwise.
print(2 in t)      # True
# 4 not in t will check if the element 4 is not present in the tuple t. It will return True if 4 is not found in the tuple, and False otherwise.
print(4 not in t)  # True
# t = (1, 2, 3, 4, 5)
# for item in t will iterate through each element in the tuple t and print it. It will print each element on a new line.
for item in t:
    print(item)

# t[1:4] will return a new tuple containing the elements from index 1 to index 3 (index 4 is not included) of the tuple t. It will return (2, 3, 4).
print(t[1:4])
# slicing