import random
import string

print("======== Password Generator ========")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

letters_length = int(input("How man letters do you want? > "))
numbers_length = int(input("How man digits do you want? > "))
symbols_length = int(input("How man symbols do you want? > "))

# Picking All Characters depending on how long the user wants
password_chars = (
  [random.choice(letters) for _ in range(letters_length)] +
  [random.choice(numbers) for _ in range(numbers_length)] +
  [random.choice(symbols) for _ in range(symbols_length)] 
)

# Shuffle the password characters to be fully randomized
random.shuffle(password_chars)

# Then join all characters together in a final result
password = ''.join(password_chars)

print("Your Password is:")
print(password)