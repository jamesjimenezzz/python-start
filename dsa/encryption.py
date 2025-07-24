

import random
import string

chars = string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
encrypt = chars.copy()
random.shuffle(encrypt)

name = "James"
cipher_text =""


for letter in name:
    index = chars.index(letter)  
    
    cipher_text += encrypt[index]



print(cipher_text)