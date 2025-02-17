# Let's first define some variables and classes
water_logo = '''     
**********************************************************
                                ,d                          
                                88                          
8b      db      d8 ,adPPYYba, MM88MMM ,adPPYba, 8b,dPPYba,  
`8b    d88b    d8' ""     `Y8   88   a8P_____88 88P'   "Y8  
 `8b  d8'`8b  d8'  ,adPPPPP88   88   8PP""""""" 88          
  `8bd8'  `8bd8'   88,    ,88   88,  "8b,   ,aa 88          
    YP      YP     `"8bbdP"Y8   "Y888 `"Ybbd8"' 88     

**********************************************************
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Script will start from here.
print(water_logo)
print(bcolors.HEADER + "This script will check if your water is boiling or not." + bcolors.ENDC)
print(bcolors.WARNING + "Please type \"f\" for Fahrenheit, 'C' for Celsius and 'K' for Kelvin." + bcolors.ENDC)

# Let's first ask the user which temp scale he/she is using.
unit = input('Which temp scale are you using? ').lower()

# Let's ask the user which temp the water currently is.
temp = float(input('Which temp is the water? '))

# Conditional statements
if unit == 'f':
    if temp >= 212:
        print('The water is boiling.')
    else:
        print('The water is not yet boiling.')
elif unit == 'c':
    if temp >= 100:
        print('The water is boiling.')
    else:
        print('The water is not yet boiling.')
elif unit == 'k':
    if temp >= 373:
        print('The water is boiling.')
    else:
        print('The water is not yet boiling.')
else: 
    print('An invalid value was used. Try running this script again.')


