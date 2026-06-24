# Write a program to store seven fruits in a list entered by the user.
fruits = []
for i in range(7):
    fruit = input(f"Enter Fruit Number {i+1} name: \n")
    fruits.append(fruit)
print(fruits)
