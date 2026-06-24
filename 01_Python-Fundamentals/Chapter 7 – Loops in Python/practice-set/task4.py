# Write a program to find whether a given number is prime or not
number = int(input("Enter a Number To Check Is It Prime Number Or Not"))
if number <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
