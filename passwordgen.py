import random
import string

uppercase = string.ascii_letters + string.punctuation + string.digits
punctuation = string.punctuation
length = int(input("Enter your password length : "))
password = ""
for i in range(length + 1):
    password += random.choice(uppercase)
print(password)