logo = r""" # USE 'r' BEFORE THE STRING TO MAKE IT A RAW STRING AND IGNORE THE BACKSLASHES (Escape Sequence errors)
              _       _     _             
             (_)     | |   | |        
__      _____ _  __ _| |__ | |_
\ \ /\ / / _ \ |/ _` | '_ \| __| 
 \ V  V /  __/ | (_| | | | | |_
  \_/\_/ \___|_|\__, |_| |_|\__|
                 __/ |                               
                |___/                                
"""
# This script will calculate your BMI based on your weight and height.
# This script will only work for the metric system.

# User input
print(logo)
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

# Calculate BMI
bmi = weight / (height * height)

# Conditional statements
if bmi < 18.5:
    print('Underweight.')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normal weight.')
elif bmi >= 25 and bmi <= 29.9:
    print('Overweight.')
elif bmi >= 30:
    print('Obese.')