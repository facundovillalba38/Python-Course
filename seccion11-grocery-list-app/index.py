#App to create a grocery list

groceryList = []
add_list = 'y'

while(add_list == 'y'):
     grocery = input("Add an item to grocery list: ")
     grocery = grocery.title()
     groceryList.append(grocery)
     add_list = input("Do you want to add another item? (y/n) ")
     add_list = add_list.lower()

print("Grocery List: ")
for item in groceryList:
     print("\t",item)

bought_food = input("What food you just bought? ")
bought_food = bought_food.title()
groceryList.remove(bought_food)

print("Current Grocery List: ")
for item in groceryList:
     print("\t",item)




