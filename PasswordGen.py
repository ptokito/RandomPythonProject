import random

print("Welcome to your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')

number = int(number)

length = input("Please enter the length of your password: ")

length = int(length)

print("\nYour password is ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
