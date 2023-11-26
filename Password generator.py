import random

print("Password Generator\n")

char ='qweasdzxcrtfgvbyuhjnmikolp124578/*963.0+-!@#$%&*?=_'

number = input('Amount of password to generate : ')
number = int(number)
length = input('Your password will length : ')
length = int(length)
print('\nHere are the passwords : \n')

for pwd in range (number):
    password = ''
    for i in range(length):
        password += random.choice(char)
    print('\n'+password)

