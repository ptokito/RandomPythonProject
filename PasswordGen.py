import random

print("Welcome to your Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789"

num = input('Amount of passwords to generate: ')

num = int(num)

length = input("Please enter the length of your password: ")

length = int(length)

print("\nYour password is ")

for pwd in range(num):
    passwords = ""
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)
