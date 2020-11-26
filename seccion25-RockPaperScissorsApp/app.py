# Rock Paper Scissors App.

import random

rps = ['Rock', 'Paper', 'Scissors']

rounds = int(input('How many rounds do you want to play? '))

user_points = 0
computer_points = 0

for round in range(rounds):
     print(f'\nRound {round}')
     print(f'User: {user_points} \t Computer: {computer_points}')
     select_user = input("Time to pick... rock, paper, scissors: ").title()
     select_computer = rps[random.randint(0,2)]
     print(select_user)
     if select_user != 'Rock' and select_user != 'Paper' and select_user !='Scissors':
          print("Invalid Choice. Point to the computer")
          computer_points += 1
     elif select_user == select_computer:
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("It is a tie!")
     elif select_user == 'Rock' and select_computer == 'Scissors':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Rock destroys Scissors. Point for user")
          user_points += 1
     elif select_user == 'Scissors' and select_computer == 'Paper':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Scissors cuts paper. Point for user")
          user_points += 1
     elif select_user == 'Paper' and select_computer == 'Rock':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Paper covers Rock. Point for user")
          user_points += 1
     elif select_computer == 'Rock' and select_user == 'Scissors':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Rock destroys Scissors. Point for computer")
          computer_points += 1
     elif select_computer == 'Scissors' and select_user == 'Paper':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Scissors cuts paper. Point for computer")
          computer_points += 1
     elif select_computer == 'Paper' and select_user == 'Rock':
          print(f"User: {select_user} \t Computer: {select_computer}")
          print("Paper covers Rock. Point for computer")
          computer_points += 1

print(f"\nFINAL SCORE: \nUser: {user_points} \t Computer: {computer_points}")