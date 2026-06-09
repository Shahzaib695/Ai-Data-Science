# Write a program to mine a log file and find out whether it contains ‘python’.
with open("task6log.txt") as f:
    verify = f.read()
if "python" in verify:
    print("Exists")
else:
    print("Not Exists")