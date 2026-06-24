# Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set();
for i in range(8):
    n = int(input(f"Enter number {i+1}: \n"));
    s.add(n)
print(s);
