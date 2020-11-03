# Print
print("Hola bb")

# Variables

x = 5
print(5)
print(x)

message = "Hola bb"
print(message)

#Strings
name = "Facundo villalba"
print(name)
print(name.upper()) #Mayuscula
print(name.lower()) #Minuscula
print(name.title()) #Inicio de cada palabra mayuscula
print(name.strip()) #Elimina espacios en el inicio o fin del string

first_name = "Facundo"
last_name = "Villalba"
print(first_name + " " + last_name) # Concatena variable con +

print(name.count('undo'))  #cuenta las veces que aparece el string que pasamos por parametro en el string original

print("The name has "+str(name.count('a'))+ " a's in it") # str() convierte un nro a string para poder concatenar
print("The name has",name.count('a'),"a's in it") # funciona igual que el de arriba, se le pasa cada fragmento como un parametro diferente

#Integers and floats


#The type() function

title = "Facundo"
num_1 = 1
num_2 = 0.2

print(type(title)) # Devuelve el tipo de dato de la variable
print(type(num_1))
print(type(num_2))

#The input() function

first_name = input("What's your name? ") #se le pide un dato por pantalla, y lo que escribe el usuario se le asigna a una variable
last_name = input("What's your last name? ")
print("Hello,",first_name.title(),last_name.title())

number = input("What is your favorite number? ")
number = int(number) # Como devuelve un string, se castea en el tipo de dato que se espera recibir. Tambien funciona con float en vez de int
print("Your favorite number is", number)
print(type(number))

# String formating method

team = "Boca Juniors"
associates = 60000
money = 10.5

# print using string concatenation
print(team + " has "+ str(associates) + " associates, and $"+str(money) +" Million Dollars.")

# print using string concatenation but with parameters instead of casting variables to str
print(team,"has",associates,"associates, and $",money,"Million Dollars.")

# print using .format() method for Strings
print("{0} has {1} associates, and ${2} Million Dollars.".format(team, associates, money))

# print using f-strings
print(f"{team} has {associates} associates, and ${money} Million Dollars.")