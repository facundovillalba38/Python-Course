# App that counts the letters included in a sentence.

print("Welcome to the Letter Counter App")

name = input("What is your name? ")
print("Hello ",name.title())

print("I will count the number of times that a specific letter appears in a message")

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

letterToCount = input("Which letter of that sentence do you want to count? ")
letterToCount = letterToCount.lower()

print("The letter",letterToCount,"is",sentence.count(letterToCount),"times in the sentence")