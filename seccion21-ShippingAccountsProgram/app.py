usernames = ['facuv12', 'user.user']

user = input("Username: ")

logged = False

for usern in usernames:
     if(usern.lower() == user.lower()):
          logged = True

if(logged):
     print("Shipping orders 0 to 100:    $5.10 each")
     print("Shipping orders 100 to 500:  $5.00 each")
     print("Shipping orders 500 to 1000: $4.95 each")
     print("Shipping orders over 1000:   $4.80 each")

     itemsToBuy = int(input("How many items would you like to ship: "))
     finalPrice = 0
     if(itemsToBuy<100):
          finalPrice = itemsToBuy * 5.10
     elif(itemsToBuy>=100 and itemsToBuy<500):
          finalPrice = itemsToBuy * 5
     elif(itemsToBuy>=500 and itemsToBuy<1000):
          finalPrice = itemsToBuy * 4.95
     elif(itemsToBuy>=1000):
          finalPrice = itemsToBuy * 4.80
     else:
          print("YOU CANNOT SELECT A NEGATIVE AMOUNT.")
     
     print(f"To ship {itemsToBuy} items it will cos you ${finalPrice} at ${finalPrice / itemsToBuy} per item.")

     placeOrder = input("Would you like to place this order (y/n): ")
     if(placeOrder == "y"):
          print(f"Okay. Shipping your {itemsToBuy} items.")
     else:
          print(f"Okay. No order is being placed at this time.")
else:
     print("Sorry. You don't have an account with us. GoodBye")

          