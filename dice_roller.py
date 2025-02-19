# Import random function
from random import randint

# Ask user for input
rolls = int(input("How many dice are we rolling? "))
sides = int(input("How many sides on each die? "))

while True:
    result = "|"
    for die in range(rolls):
        rand = randint(1, sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? ('q' to quit) ")
    if reply == "q":
        break
