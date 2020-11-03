import cmath

# Display the solution to any number of quadratic equations


print("Welcome to the quadratic solver app \n\n" )
print("A quadratic ecuation is of the form ax^2 + bx + c = 0\n")
print("Your solutions can be real or complex numbers.\n")
print("A complex number has two parts: a + bj \n")
print("Where a is the real portion and bj is the imaginary portion.")

quantity = int(input("How many equations would you like to solve today: "))

for num in range(quantity):
     a = float(input("Please enter the value of a (coefficient of x^2): "))
     b = float(input("Please enter the value of b (coefficient of x): "))
     c = float(input("Please enter the value of c (coefficient): "))
     x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
     x2 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)

     print("\nThe solutions to",a,"x^2+",b,"x+",c,"=0 are: ")
     print("\n\t x1 =", x1)
     print("\t x1 =", x2)
     

