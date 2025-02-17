## ask age of person
age = input("How old are you? ")

age_in_float = float(age)
age_in_days = age_in_float * 365

print("You are " + str(age_in_days) + " days old.")