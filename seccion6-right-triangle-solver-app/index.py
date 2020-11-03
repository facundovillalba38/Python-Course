# App to calculate area and hypotenuse of a triangle

print("Welcome to the Right Triangle Solver App")

side1 = input("Enter the first leg of a triangle: ")
side2 = input("Enter the second leg of a triangle: ")

side1 = float(side1)
side2 = float(side2)

# a^2 + b^2 = c^2 -> Hipotenusa

hypotenuse = (side1**2+side2**2)
hypotenuse = round(hypotenuse,3)

area =  (side1 * side2)/2
area = round(area,3)

print("The hypotenuse of the triangle is:",hypotenuse)
print("The area of the triangle is:",area)

