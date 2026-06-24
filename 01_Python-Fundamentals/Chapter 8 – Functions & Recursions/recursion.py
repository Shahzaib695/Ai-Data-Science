# Recursion means a function calling itself to break a problem down.
def factorial(n):
    # -------------------------------------------------------------
    # STEP 1: THE BASE CASE (The Stop Sign)
    # This prevents the function from calling itself forever.
    # When 'n' drops to 1 or 0, we stop and start returning answers.
    # -------------------------------------------------------------
    if n == 1 or n == 0:
        return 1
    
    # -------------------------------------------------------------
    # STEP 2: THE RECURSIVE CASE (The "Loop" Mechanism)
    # The function multiplies 'n' by the result of calling itself 
    # with a smaller number (n - 1). This shrinks 'n' on every turn
    # until it hits the base case.
    # -------------------------------------------------------------
    return n * factorial(n - 1)

# Taking input from the user
n = int(input("Enter a number: "))

# Printing the final result after all the recursive layers finish
print(f"The factorial of number {n} is {factorial(n)}")

def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n
print(sum(n))