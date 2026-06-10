# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class attribute:
    a = 10
obj = attribute
print(obj.a)
obj.a = 20
print(obj.a)
print('''The answer of this task is a clear no
      As the class elements are intact if we move it towards.
      To another variable the attributes value remains same''')