# App to list your favs teachers

teacher = []

t1 = input("Enter your first fav teacher: ")
teacher.append(t1.title())

t2 = input("Enter your second fav teacher: ")
teacher.append(t2.title())

t3 = input("Enter your third fav teacher: ")
teacher.append(t3.title())

print("Your favs teachers ranked are", teacher)
#teacher.sort()
print("Your favs teachers alphabetically are: ", sorted(teacher))
#teacher.reverse()
print("Your favs teachers in reverse alphabetically order are: ", sorted(teacher, reverse=True))


print("Oh no,",teacher[0],"is no longer your favorite teacher.")
new_fav = input("Enter your new favorite teacher: ")
teacher.insert(0, new_fav.title())

print("Your favs teachers ranked are", teacher)
#teacher.sort()
print("Your favs teachers alphabetically are: ", sorted(teacher))
#teacher.reverse()
print("Your favs teachers in reverse alphabetically order are: ", sorted(teacher, reverse=True))

deleted_teacher = input("You've decided you no longer like a teacher. Which teacher would you like to remove? ")
teacher.remove(deleted_teacher.title())
print("Your favs teachers ranked are", teacher)
#teacher.sort()
print("Your favs teachers alphabetically are: ", sorted(teacher))
#teacher.reverse()
print("Your favs teachers in reverse alphabetically order are: ", sorted(teacher, reverse=True))



