marks = {
    "Shahzaib" : 90,
    "Munawar" : 87,
    "Saim" : 76,
    "Yashir" : 14
}
print(marks,type(marks))
# you can not print like marks[0] because in dictionary you have keys named as shahzaib yashir so printing through index means is not possible
print(marks["Yashir"])
print('''PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.''')