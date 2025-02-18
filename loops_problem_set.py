#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for i in word:
    print(i)

# Write a while loop that does the same thing!
count = 0

while not count == len(word):
    print(word[count])
    count += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
count = 100

while not count == 140:
    print(count)
    count += 2

# Write a for loop that does the same thing (with range())
for i in range(100, 142, 2 ):
    print(i)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply
passphrase = "sillygoose"
input_user = input("Give the passphrase to enter: ")

while not input_user == passphrase:
    input_user = input("Try again: ")

print("Welcome.")

