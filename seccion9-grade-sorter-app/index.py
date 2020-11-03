# App to sort your grades in 4 years

print("Welcome to the Grade Sorter App")

grades = []

grade1 = input("What is your first grade (0-100): ")
grades.append(int(grade1))
grade2 = input("What is your second grade (0-100): ")
grades.append(int(grade2))
grade3 = input("What is your third grade (0-100): ")
grades.append(int(grade3))
grade4 = input("What is your fourth grade (0-100): ")
grades.append(int(grade4))

print("Your grades are", grades)
grades.sort() # lo ordena
grades.reverse() # invierte el orden
print("Your grades from highest to lowest are: ", grades)

print("Your best grade is: ",max(grades))
print("Your lowest grade is: ",min(grades))


print("Your lowest two grades will be dropped now")
removed1 = grades.pop()
print("Removed Grade: ",removed1)
removed1 = grades.pop()
print("Removed Grade: ",removed1)

print("Your remaining grades are: ", grades)









