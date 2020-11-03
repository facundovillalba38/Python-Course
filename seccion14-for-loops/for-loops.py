# Looping through a list with a for loop

teams = ['Boca', 'Real Madrid', 'Liverpool', 'Bayern Munich']
print(teams)
print(type(teams))

for team in teams:
     print(team.title())



triples = [['a','b','c'],['1','2','3'],['do','re','mi']]

for list_value in triples:
     for element in list_value:
          print(element, end=' ')
     print("First loop finished")

print("Finish all")


values = range(1,10)
for i in values: # values es range(1,10)
     print(i, end=' ')

for i in range(1,10, 2):
     print("\n",i, end=' ')

message = "Hello World"
list_message = list(message) # separa la palabra diviendola por caracter
print(list_message)

new_message = ''.join(list_message)
print(new_message)

numbers = list(range(10,101, 10))
print(numbers)

squares = []
for number in numbers:
     print(number)
     square = number**2
     squares.append(square)

print(squares)
for square in squares:
     print(square)

cubes = [number**3 for number in numbers] # es lo mismo que hacerlo dentro de un for, pero mas corto, buena opcion
print(cubes)
for cube in cubes:
     print(cube)

print(min(cubes)) #menor de cubo
print(max(cubes)) #mayor de cubo
print(sum(cubes)) #suma de todos los cubos

#List slicing

print(cubes)
for cube in cubes[0:2]: # recorre solo el rango indicado de la lista (no incluye el ultimo)
     print(cube)

# Si quiero igualar una lista a otra variable, debo hacerlo de la siguiente forma
# list1 = list2 [:] O list1 = list2.copy() y ahi hace una copia exacta 
# si lo hacemos sin el "[:]" entonces se referencia a la lista a la que se lo esta igualando, por lo que si realizamos cualquier modificacion, tambien se verá afectada la lista original. Por eso es que se hace de la forma indicada mas arriba

# The ZIP function

names = ["Facundo", "Pepe", "Juan", "Maria"]
ages = [33,22,55,12]

for i in range(len(names)):
     print(names[i],":",ages[i],"years old")

# zip()
for name, number in zip(names,ages):
     print(name.title(),":",number,"years old")

