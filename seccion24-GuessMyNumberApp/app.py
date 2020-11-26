#Guess my number App

import random

print("Hi! I am thinking of a number between 1 and 20")
rand_number = random.randint(1, 20)

for i in range(1, 6):
     guess = int(input("Take a guess: "))
     if guess == rand_number:
          print(f"Excelent, you guessed the number in {i} guesses!")
          break
     elif guess < rand_number:
          print("The guess is to low.")
     elif guess > rand_number:
          print("The guess is to high.")
     if i == 5:
          print(f"GAME OVER. The number i was thinking was {rand_number}")


