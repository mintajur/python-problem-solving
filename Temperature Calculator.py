print("-----------------------------------------")
print("|                                        |")
print("|           Temperature Calculator       |")
print("|                                        |")
print("-----------------------------------------")
print("Insert F to calculate Fahrenheit and insert C for Celsius: ")
selection = input()
if selection.upper() == "F":
    print("Insert your value in Fahrenheit: " )
    Celsius = float(input())
    celsius = (Celsius - 32) * 5/9
    print("Your celceius value is: ", celsius)
elif selection.upper() == "C":
    print("Insert your value in Celsius: ")
    Fahrenheit = float(input())
    fahrenheit = Fahrenheit * (9/5) + 32
    print("Your Fahrenheit value is: ", fahrenheit)
else:
    print("There is an unexpected error!")