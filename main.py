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

# Asking the user for the password length
# passowrd_length = int(input("How long should the password be? > "))

all_symbols = letters + numbers + symbols
remaining_chars = len(password_chars) - (letters_length + numbers_length + symbols_length)

# Conecatinating Characters with the password_chars
password_chars += [random.choice(all_symbols) for _ in range(max(remaining_chars, 0))]

# Shuffle the password characters to be fully randomized
random.shuffle(password_chars)

# Then join all characters together in a final result
password = ''.join(password_chars)

print("Your Password is:")
print(password)