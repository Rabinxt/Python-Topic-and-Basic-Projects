import string
import random

chars =" " +string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPT

plain_text = input("Enter the message : ")
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Cipher Text : {cipher_text}")
