import random

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

while (dice_1 != 1) or (dice_2 != 1):
    print("*" * 15)
    print('Rolling dice.')
    print(f"Dice 1: {dice_1}\nDice 2: {dice_2}")
    print("*" * 15)
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

print("*" * 15)
print("SNAKE EYES!!")
print(f"Dice 1: {dice_1}\nDice 2: {dice_2}")
print("*" * 15)
