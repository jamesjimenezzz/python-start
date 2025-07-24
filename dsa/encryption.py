

import random
import string

chars = string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
encrypt = chars.copy()
random.shuffle(encrypt)

name = input("Enter a message to encrypt ")
cipher_text =""


for letter in name:
    index = chars.index(letter)  
    
    cipher_text += encrypt[index]


print(f"Original Message: {name}")
print(f"Encrypted Message: {cipher_text}")


#DECRYPTION


cipher_text = input("Enter a message to decrypt ")
name = ""


for letter in cipher_text:
    index = encrypt.index(letter)  
    
    name += chars[index]


print(f"Encrypted Message: {cipher_text}")
print(f"Original Message: {name}")
