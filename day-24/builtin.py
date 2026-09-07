import random

name = input('enter the name:').title()
dob = input('enter the date of birth[DD-MM-YYYY]:')
spl = ['@','#','$','%','*','+','.',',']

password = name+random.choice(spl) + dob[-4:]

print('Generated password:',password)
