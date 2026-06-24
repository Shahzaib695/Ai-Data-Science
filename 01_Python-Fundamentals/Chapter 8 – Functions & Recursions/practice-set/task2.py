# Write a python program using function to convert Celsius to Fahrenheit.
Celsius = float(input("Enter the temperature in Celsius: "))
def conversion(Celsius):
    print("Lets COnvert It into Farenhite")
    fahrenheit = (Celsius * 9/5)+32
    return fahrenheit
result = print(conversion(Celsius))