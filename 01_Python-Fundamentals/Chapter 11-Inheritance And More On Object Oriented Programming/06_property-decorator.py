class Employee:
    a = 1
    # class method -understood
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    # property decorator name ke andar show kra ke kuch horha hai iske nieche phir hamne setter ko use kra to set names deep understanding of oop is required
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.fname, e.lname)
e.show()
# sahi samaj nahi aya 