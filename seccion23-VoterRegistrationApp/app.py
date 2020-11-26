# Voter registration App

name = input("Hello, what is your name? ")
age = int(input("How old are you? "))

political_parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

if age<18:
     print("You are not older enough to affiliate a partie.")
else:
     print("Here is a list of the political parties availables:")
     for parties in political_parties:
          print(f"\t-{parties}")
     party = input("Which partie would you like to join? ").title()
     if party in political_parties:
          print(f"Congratulations! You join to {party}!")
          if party == 'Republican' or party == 'Democratic':
               print("This party is a major party")
          else:
               print("This party is not a major party")
     else:
          print("I'm sorry, that party doesn't exists")