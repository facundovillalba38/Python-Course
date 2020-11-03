# App to do a multiplication or exponentiation table

print("Welcome to multiplication/exponentiation table app")

number = input("Enter the number to get the multiplication and exponentiation tables: ")
number = float(number)
number = round(number,2)

print("\nMultiplication Table: ")

for x in range(1,10):
     print(number,"*",x,"=",round(number*x,2))

print("\nExponentiation Table: ")
for x in range(1,10):
     print(number,"**",x,"=",round(number**x,2))