# All of these Comprehensions are used to create List, Dictionary and set. But you don’t have to use multiple lines of code for loops and If-Else statements. 
# its just like a ternary operator
# for example we are writing a code to add even numbers in a list
l1 = []
for i in range(1,21):
    if i % 2==0:
        l1.append(i)
    else:
        print("Cant add in the list condition not satisfied")
print(l1)
# list comprehension will help us to write all this code in a single line
# [(the thing u want to append) the loop setup then if else setup]
l1 = [i for i in range(1,21) if i % 2== 0]
print(l1)
# Dictionary Comprehension
# now lets print a dictionary with numbers and in those keys there will be there powers
d1 = {}
for i in range(1,11):
    d1[i] = i ** 2
print(d1)
# the key there values then loop
d1 = {i : i**2 for i in range(1,11)}
print(d1)
# Set Comprehension
# similar to list/dict comprehensions but creates a set
# example: even numbers from 1 to 20
s1 = {i for i in range(1,21) if i % 2 == 0}
print(s1)
# example: squares as a set (duplicates removed automatically)
# normal method first
s2 = set()
for i in range(1,11):
    s2.add(i**2)
print(s2)

# set comprehension (concise)
s2 = {i**2 for i in range(1,11)}
print(s2)
