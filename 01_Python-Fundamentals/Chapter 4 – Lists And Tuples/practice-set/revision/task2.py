# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = [];
for i in range(6):
    mark = input(f"Enter Marks Of Student {i+1} \n");
    marks.append(mark)
marks.sort()
print(marks)