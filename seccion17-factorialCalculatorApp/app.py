# app to calculate factorial of a number
import math

print("Welcome to de factorial calculator app")

factorial = int(input("What number would you like to compute the factorial of? "))

print(factorial,'!=', end="")


result = 1
for i in range(1, factorial+1):
     print(i, end="*")
     result=result*i 

print("\nThe factorial of 10 is",result)    


fact = math.factorial(factorial)
print("\nThe factorial of 10 is",fact)    