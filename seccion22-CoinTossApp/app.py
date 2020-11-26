# Coin Toss App

import random

print("Welcome to CoinToss App")

print("I will flip a coin a set number of times.")

flip_number = int(input("How many times would you like to flip coin? "))

choice = input("Would you like to see the result of each flip? (y/n) ").lower()



heads = 0
tails = 0

if choice.startswith("y"):
     print("Flipping!")
     for flip in range(flip_number):
          coin = random.randint(0,1)
          if(coin == 0):
               print("HEADS")
               heads += 1
          else:
               print("TAILS")
               tails += 1
          if(heads == tails):
               print("At this points, you have the same number of heads than tails.")
else:
     print("Thank you for coming! GoodBye!")

     



