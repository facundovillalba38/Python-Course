# App to convert Fahrenheit to Celsius and Kelvin

print("Welcome to the Temperature Conversion App")

fahrenheit = input("Please enter the temperature in Fahrenheit: ")

celsius = (float(fahrenheit)-32)*(5/9)
celsius = round(celsius, 2)

kelvin = celsius + 273.15
kelvin = round(kelvin,2)

print("Fahrenheit:",fahrenheit,"º F")
print("Celsius:",celsius,"º C")
print("Kelvin:",kelvin,"º K")