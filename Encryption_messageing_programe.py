import random
import string

chars =  string.punctuation + string.digits + string.ascii_letters  + " " 
chars = list(chars)
key = chars.copy()

random.shuffle(key)


user_input = input("Enter a message to encrypt: ")
encrypted_messegee = ""

for letter in user_input:
    index = chars.index(letter)
    encrypted_messegee += key[index]

print(f"original message : {user_input}")
print(f"encrypted message: {encrypted_messegee}")


encrypted_messegee = input("Enter a message to encrypt: ")
user_input = ""

for letter in encrypted_messegee:
    index = key.index(letter)
    user_input += chars[index]

print(f"encrypted message: {encrypted_messegee}")
print(f"original message : {user_input}")
