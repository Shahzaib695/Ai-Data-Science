# Write a program to accept marks of 6 students and display them in a sorted manner.
marks= [];
# logic range here means index i mean ke 0 se 5 tk ayega 6 ko chorke total 1 till 6 ke number store horhe
for i in range (6):
    mark = int(input(f"Enter marks of studnet {i+1}:\n"))
    marks.append(mark);

marks.sort();
print(marks)