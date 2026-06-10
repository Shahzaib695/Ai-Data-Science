# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,field):
        self.name = name;
        self.field = field
    def details(self):
        print(f"The name of the employee working at {self.company} is {self.name}. The Employee Working Field is {self.field}")

p = Programmer("Shahzaib","Artifical Intelligence")
p1 = Programmer("Munawar","Software Engineering")        
p2 = Programmer("Yashir","Deployment Operations")
p.details()        
p1.details()        
p2.details()        
