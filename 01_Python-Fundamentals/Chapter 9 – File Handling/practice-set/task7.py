with open("task6log.txt","r") as f:
    line_number = 1

    for line in f:
        if "python" in line.lower():
            print("Found at Line ",line_number)
        
        line_number += 1