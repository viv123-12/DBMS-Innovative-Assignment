# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:55:28 2022

@author: vivek
"""

from Crypto.Cipher import DES
from secrets import token_bytes
import codecs

key = token_bytes(8)
def encrypt(msg):
    cipher=DES.new(key,DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag
def decrypt(nonce, ciphertext, tag):
    
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
nonce , ciphertext , tag =encrypt(input("Enter a message:"))
plaintext = decrypt(nonce, ciphertext, tag)
codecs.decode(ciphertext, 'UTF-16')

print(f'cipher text:{ciphertext}')
print("Plaintext is:",plaintext)
