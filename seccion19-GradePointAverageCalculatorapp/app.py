print("Welcome to the Average Calculator App")

name = input("What is your name: ")
grades = int(input("How many grades would you like to enter: "))

gradesList = []

for i in range(grades):
     grade = int(input("Enter grade: "))
     gradesList.append(grade)

gradesList.sort()
gradesList.reverse()

print("Grades - Highest to Lowest")
for grade in gradesList:
     print('\t\t',grade)

print(name, "Grade Summary: ")
print("\tTotal Number of Grades: ",grades)
print("\tHighest Grade:",max(gradesList))
print("\tLowest Grade:",min(gradesList))
avg = sum(gradesList)/len(gradesList)
print("\tAverage:",avg)

desiredAvg = float(input("What is your desired avg: "))
gradeRequired = desiredAvg*(len(gradesList)+1) - sum(gradesList)
gradeRequired = round(gradeRequired, 2)

if(gradeRequired < 100):
     print("\You will need to get a", gradeRequired,"on your next assignment to get a",desiredAvg,"avg")
else: 
     print("\You will need to get more than a 100 in your next assignment, I'm sorry, but that is impossible")

new_grades = gradesList[:]
grade_change = float(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = float(input("What grade would you like to change "+str(grade_change)+" to: "))
new_grades.append(new_grade)

new_grades.sort()
new_grades.reverse()

print("Grades - Highest to Lowest")
for grade in new_grades:
     print('\t\t',grade)

print(name, "Grade Summary: ")
print("\tTotal Number of Grades: ",grades)
print("\tHighest Grade:",max(new_grades))
print("\tLowest Grade:",min(new_grades))
avg = sum(new_grades)/len(new_grades)
print("\tAverage:",avg)

print("\nOriginal Grades: ",gradesList)