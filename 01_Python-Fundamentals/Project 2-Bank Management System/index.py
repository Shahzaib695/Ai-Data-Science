import json
import random
import string
from pathlib import Path
# to make it exceptionally good we are going to use info.json as our database and we will be using a local variable info to dump that info inside of it. IK this approach is a bit complicated but trust me its way good
class Bank:
    database = 'data.json'
    data = []

    try:
        # dumped info stored in json inside of info variable
        # safteying the operation
        if Path(database).exists():
            print("File loaded")
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("File do not exists")
    except Exception as err:
        print(f"An error occured {err}")   
    @classmethod
    # lets make this method private as we want nobody to access it and i am replacing the method to class
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))  
    @classmethod
    def __generateAccountNumber(cls):
        # we will be using a combo of numbers and alphabets
        # k = number of elements
        alphabets = random.choices(string.ascii_letters,k=3)
        numbers  = random.choices(string.digits,k=3)
        id = alphabets + numbers
        return "".join(id)

    def create(self):
        info = {
            "name" : input("Enter Your Name: "),
            "age" : int(input("Enter Your Age")),
            "email" : input("Enter Your Email"),
            "pin" : int(input("Enter A 4 digit pin that u want for your account")),
            "Account.No" : Bank.__generateAccountNumber(),
            "balance" : 0 
        }
        if info["age"] < 18:
            print("You can not create your account because you are below the legal age")
        elif len(str(info["pin"])) != 4:
            print("You might have entered the pin less than 4 times or more than 4 times")
        elif "@" not in info["email"]:
            print("Invalid Email Address Has Been Entered")
        else:
            print("Account Created Successfully\n")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down all your details specifically the account number")
            Bank.data.append(info)
            # for updating the database we are going to call a static method to push changes to json file look above in the class
            Bank.__update()
    def depositMoney(self):
        account = input("Enter Account Number")
        pin = int(input("Enter Your 4 digit Pin"))
        userData = [i for i in Bank.data if i["Account.No"] == account and i["pin"] == pin]
        if userData == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much Money You Want To Deposit: "))
            if amount < 0:
                print("Enter amount above 0")
            else:
                userData[0]["balance"] += amount
                Bank.__update()
                print("Amount Depositied Successfully")


        
    def withdraw(self):
        account = input("Enter Account Number")
        pin = int(input("Enter Your 4 digit Pin"))
        userData = [i for i in Bank.data if i["Account.No"] == account and i["pin"] == pin]
        
        if userData == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much Money You Want To Withdraw: "))
            if amount > userData[0]['balance']:
                print("You dont have enough money")
            else:
                userData[0]["balance"] -= amount
                Bank.__update()
                print("Amount Withdrew Successfully")
    def details(self):
        account = input("Enter Account Number")
        pin = int(input("Enter Your 4 digit Pin"))
        userData = [i for i in Bank.data if i["Account.No"] == account and i["pin"] == pin]
        print("Your information is as follows: \n\n")
        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")
    def updateDetails(self):
        account = input("Enter Account Number")
        pin = int(input("Enter Your 4 digit Pin"))
        userData = [i for i in Bank.data if i["Account.No"] == account and i["pin"] == pin]
        print("Your information is as follows: \n\n")
        if userData == False:
            print("Sorry No Data Found")
        else:
            print("You can not change your account number, balance and age\n")
            print("Fill in the details to update your data or press enter to skip if u dont want to update certain details\n")
            newdata = {
                "name" : input("Enter Your New Name"),
                "email" : input("Enter Your New Email"),
                "pin" : input("Enter Your New Pin")
            }
            if newdata["name"] == "":
                newdata["name"] = userData[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userData[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userData[0]["pin"]
            newdata['age'] = userData[0]['age']
            newdata['Account.No'] = userData[0]['Account.No']
            newdata['balance'] = userData[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin']) # type: ignore

            for i in newdata:
                if newdata[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newdata[i]
            Bank.__update()
            print("Details Updated Successfully")


    def delete(self):
        account = input("Enter Account Number")
        pin = int(input("Enter Your 4 digit Pin"))
        userData = [i for i in Bank.data if i["Account.No"] == account and i["pin"] == pin]
        print("Your information is as follows: \n\n")
        if userData == False:
            print("Sorry No Data Found")
        else:
            print("Press Y for deleting and N for Not deleting")
            check = input()
            index = Bank.data.index(userData[0])
            Bank.data.pop(index)
            print("Account deleted")
            Bank.__update()
user = Bank()
print("=============================================\n")
print("Welcome to our Bank Management System \n\n")
print("Press 1 for Creating An Account \n")
print("Press 2 for Depositing Money In Your Account \n")
print("Press 3 for Withdrawing Money In Your Account \n")
print("Press 4 for Seeing Your Account Details \n")
print("Press 5 for Updating Your Account Details \n")
print("Press 6 for Deleting Your Account \n")

choice = int(input("Enter your desired choice number \n"))
if choice == 1:
    user.create()
elif choice == 2:
     user.depositMoney()
elif choice == 3:
     user.withdraw()
elif choice == 4:
     user.details()
elif choice == 5:
     user.updateDetails()
elif choice == 6:
     user.delete()