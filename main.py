import random
import string

print("======== Password Generator ========")
symbols = string.ascii_letters + string.digits + string.punctuation
length = int(input("How long should the password be? > "))
password = ""

for i in range(length):
  password += random.choice(symbols)

print("Your Password is:")
print(password)