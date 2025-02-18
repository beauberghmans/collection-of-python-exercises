# Bottles of beer song in a for loop
sentence_1 = "bottles of beer on the wall."
sentence_2 = "bottles of beer."
sentence_3 = "Take one down, pass it around,"

for i in range(99,0,-1):
    print(f"{i} {sentence_1}")
    print(f"{i} {sentence_2}")
    if i > 1:
        print(f"{sentence_3} {i-1} {sentence_1}")
    else:
        print(f"{sentence_3} no more {sentence_1}")
    print("*" * 30)

# Bottles of beer in a while loop
sentence_1 = "bottles of beer on the wall."
sentence_2 = "bottles of beer."
sentence_3 = "Take one down, pass it around,"

count = 99

while count > 0:
    print(f"{count} {sentence_1}")
    print(f"{count} {sentence_2}")
    if count > 1:
        print(f"{sentence_3} {count-1} {sentence_1}")
    else:
        print(f"{sentence_3} no more {sentence_1}")
    print("*" * 30)
    count -= 1