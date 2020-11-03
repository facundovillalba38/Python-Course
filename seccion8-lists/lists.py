# Lists (arrays)

list = [1,2,"tres", 2.4]
print(list)
print(type(list))

new_list = [5, 50, 55, 59]

list[2] = 3
print(list)

# Lists Functions

list.append("rita la salvaje") # agrega un elemento al final
print(list)
list.insert(0, "la nueva primer posicion") # inserta un nuevo elemento en la posicion indicada
print(list)
list.remove(2.4) # elimina el elemento si coincide con lo que le pasamos (sino tira error)
print(list)
removed = list.pop()  # elimina el ultimo elemento de la lista y lo retorna
print("Removed: ",removed)
print(list)
removedByIndex = list.pop(1)  # elimina el elemento de la lista que corresponde al indice pasado por parametro y lo retorna
print("Removed By index: ",removedByIndex)
print(list)
del list[0] # otra forma de eliminar pasando indices por parametro
print(list)

# Sorting Lists

list2 = [11,2,3, 1.4]
print("\n",list2)
print(sorted(list2))  # la ordena TEMPORARIAMENTE de menor a mayor (con str tmb funca), despues vuelve a su valor original
print(sorted(list2, reverse=True))  # la ordena TEMPORALMENTE de mayor a menor (con str tmb funca), despues vuelve a su valor original
print(len(list2)) # longitud de la lista
list2.sort() # la ordena PERMANENTEMENTE de menor a mayor
print(list2)
list2.sort(reverse=True) # la ordena PERMANENTEMENTE de mayor a menor
print(list2)
list2.reverse() # la ordena de reversa a como esta actualmente
print(list2)

# Tuples (like list but immutables (you cannot change it once created, the only way to change a tuple, is override it))

numbers = (1,2,3,4) # Se utilizan parentesis en vez de corchetes
print(numbers)
print(type(numbers))