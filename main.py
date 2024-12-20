import random

letters = ['a', 'b', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to my PyPassword Generator!")
num_letters = int(input("How many letters do you want your password to contain? \n"))
num_numbers = int(input("How many numbers do you want your password to contain? \n"))
num_symbols = int(input("How many special symbols do you want your password to contain? \n"))

password_list = []

for letter in range (0, num_letters):
    password_list.append(random.choice(letters))

for number in range (0, num_numbers):
    password_list.append(random.choice(numbers))

for symbol in range (0, num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)

print(password)

