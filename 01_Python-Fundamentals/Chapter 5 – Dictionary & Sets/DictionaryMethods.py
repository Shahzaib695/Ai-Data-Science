# you can use any data type in key 
marks = {
    "Shahzaib" : 90,
    "Munawar" : 87,
    "Saim" : 76,
    "Yashir" : 14,
    0 : 114
}
print(marks[0])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Yashir":69, "Ramish":100})
print(marks)
print(marks.get("Munawar"))
# for more methods use chatgpt and other resources