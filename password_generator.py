import string
from random import choice

# All character
character = string.printable

# Correct password
unique_password = set()
count = 0

# Input from the User
print('--------------------------------------------------------------------')
no_of_password = int(input('Enter the Number of password you want ---> '))
password_length = int(input('Enter the password length ---> '))
print('--------------------------------------------------------------------')

# Random selection of character
def random_character(character):
    return (choice(character))

# Generate length of password by user input
def password_generator(password_length, character):
    password = ''
    for i in range(password_length):
        char = random_character(character)
        password += char
    unique_password.add(password)  


# Number of password
while  True:
    password_generator(password_length, character)
    if no_of_password != len(unique_password):
        continue
    else:
        break

# All password
for password in unique_password:
    count += 1
    print(f'{count} Password ---> {password}')