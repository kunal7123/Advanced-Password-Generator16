import random
import string

print("==== Advanced Password Generator ====")

length = int(input("Password Length: "))

use_upper = input("Include Uppercase? (y/n): ").lower() == 'y'
use_numbers = input("Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

characters = string.ascii_lowercase

if use_upper:
    characters += string.ascii_uppercase

if use_numbers:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)

# Strength Checker
strength = "Weak"

if length >= 8:
    strength = "Medium"

if length >= 12 and use_upper and use_numbers and use_symbols:
    strength = "Strong"

print("Password Strength:", strength)

# Save Password
save = input("\nSave password to file? (y/n): ")

if save.lower() == 'y':
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved successfully!")
    
    
    
print("\nThank you for using Advanced Password Generator!")