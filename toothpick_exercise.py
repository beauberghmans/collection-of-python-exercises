name_p1 = input("Enter player 1's name: ")
name_p2 = input("Enter player 2's name: ")

while True:
    toothpicks = 13
    result = "|" * toothpicks
    print(result)
    print(f"There are {toothpicks} toothpicks left.")

    for i in range(toothpicks):
        reply_p1 = int(input(f"How many do you take, {name_p1}? "))
        while reply_p1 != 1 and reply_p1 != 2 and reply_p1 != 3:
            reply_p1 = int(input(f"You can only take 1, 2, or 3: "))
        toothpicks -= reply_p1
        if toothpicks > 0:
            result = "|" * toothpicks
            print(result)
            print(f"There are {toothpicks} toothpicks left.")
        else:
            print(f"{name_p1} wins!")
            break

        reply_p2 = int(input(f"How many do you take, {name_p2}? "))
        while reply_p2 != 1 and reply_p2 != 2 and reply_p2 != 3:
            reply_p2 = int(input(f"You can only take 1, 2, or 3: "))
        toothpicks -= reply_p2
        if toothpicks > 0:
            result = "|" * toothpicks
            print(result)
            print(f"There are {toothpicks} toothpicks left.")        
        else:
            print(f"{name_p2} wins!")
            break
    break

print(f"GAME OVER!")