# Write a program to store seven fruits in a list entered by the user.
# print("Enter 7  fruits names in the list:\n");
# fruits = input([]);
# print(fruits)
# wrong approach we can solve this using multiple approach we will not use for loop now as we havent studied it till yet but i will definetly show that here
# using the split method
# print("Enter 7  fruits names in the list:\n");
# fruits = input("Enter Items seprated by spaces:").split();
# print(fruits);
# Its an okay approach not ideal
# another approach
# fruits = [];
# f1 = input("Enter Fruit Name");
# fruits.append(f1);
# f2 = input("Enter Fruit Name");
# fruits.append(f2);
# f3 = input("Enter Fruit Name");
# fruits.append(f3);
# f4 = input("Enter Fruit Name");
# fruits.append(f4);
# f5 = input("Enter Fruit Name");
# fruits.append(f5);
# f6 = input("Enter Fruit Name");
# fruits.append(f6);
# f7 = input("Enter Fruit Name");
# fruits.append(f7);
# print(fruits)
# the best approach
fruits = [];
for i in range (7):
    fruit = input(f"Enter Fruit {i+1} name: \n")
    fruits.append(fruit);
print(fruits);