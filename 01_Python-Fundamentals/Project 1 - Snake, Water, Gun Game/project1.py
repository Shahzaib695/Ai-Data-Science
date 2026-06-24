import random
choices = ["snake","water","gun"]

def getUserChoices():
    user_Input = input("Enter Your Choice snake,water or gun: ");
    if user_Input not in choices:
        print("Invalid Choice")
        return None
    return user_Input

def computerInput():
    return random.choice(choices)

def decideWinner(user_input,computer_input):
    if(user_input == computer_input):
        print("Draw")
    elif(user_input == "snake" and computer_input == "water") or (user_input == "water" and computer_input == "gun") or (user_input == "gun" and computer_input == "snake"):
        return "User Win"
    else:
        return "Computer Win"
    
def playGame():
    user_input = getUserChoices()
    if user_input is None:
        print("Invalid Output")
        return
    computer_input = computerInput()
    print("Computer Chose: ",computer_input)
    result = decideWinner(user_input,computer_input)
    print(result)

playGame()
    