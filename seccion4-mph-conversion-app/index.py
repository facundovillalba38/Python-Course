# App to convert miles per hour to meters per second

print("Welcome to MPH to MPS Conversion App")

mph = input("What is your speed in Miles per hour? ")

mps = float(mph) * 0.44704
mps = round(mps, 4)

print("Your speed in meters per second is", mps)