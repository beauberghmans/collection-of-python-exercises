# Ask user his/her first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# Strip first and last name of leading and trailing whitespace
first_name = first_name.strip()
last_name = last_name.strip()

# Calculate length of first and last name and store it in a new variable
full_name_length = len(first_name) + len(last_name)

# Compare lentgh of full name with length of the avarege European full name, which is 12.
# Conditions will be checked by using if, elif and else statements
print('*' * 60)
if full_name_length > 12:
    print('Your name is longer than the average European name.')
elif full_name_length < 12:
    print('Your name is shorter than the average European name.')
else:
    print('Your name is exactly as long as the average European name.')
print('*' * 60)