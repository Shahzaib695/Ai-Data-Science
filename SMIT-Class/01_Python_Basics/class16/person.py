class Person:
    def __init__(self, name, height, age, weight, gender):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
        self.gender = gender

    def full_info(self):
        print(f'''Your name is {self.name}
Your age is {self.age}
Your height is {self.height}
Your weight is {self.weight}
Your gender is {self.gender}''')

    def set_age(self, new_age):
        if new_age < 0 or new_age > 120:
            print("Error: Please enter a realistic age between 0 and 120.")
        else:
            self.age = new_age
    def get_age(self):
        return self.age;
