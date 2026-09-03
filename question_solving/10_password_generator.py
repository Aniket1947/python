import random

# Define character sets for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Get user input for password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# --- Strong Password Generator Script ---
# (This script generates a password in a fixed order: letters, then symbols, then numbers)
# It is simpler but less "strong" than the complex script because it's predictable.
print("\n# strong password generator script")
password = ""

# Add random letters
for char in range(0, nr_letters):
    password += random.choice(letters)

# Add random symbols
for char in range(0, nr_symbols):
    password += random.choice(symbols)

# Add random numbers
for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)


# --- Complex Password Generator Script ---
# (This script generates characters into a list and then shuffles them for true complexity)
print("\n# complex password generator script")
password_list = []

# Add letters to the list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add symbols to the list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers to the list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Optional: Print the unshuffled list to see the components
# print(password_list) 

# Shuffle the list to randomize the character order
random.shuffle(password_list)

# Optional: Print the shuffled list
# print(password_list)

# Join the list of characters into a single string
password = ""
for char in password_list:
    password += char

print(f"\nYour Complex Password is: {password}")