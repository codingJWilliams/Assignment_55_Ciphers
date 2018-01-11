#!/usr/bin/python
# -*- coding: utf-8 -*-
import doctest
import base64

alphabet = [chr(x) for x in range(32, 127)]

class Cipher:
    name = 'Vigenere Cipher'
    desc = 'Ceasar shift with a key that selects the shift amount'
    def encodeFriendly():
        plaintext = input(' Text to encode > ')
        key = input(' Key > ')
        return Cipher.encode(plaintext, key)

    def decodeFriendly():
        plaintext = input(' Ciphertext to decode > ')
        key = input(' Key > ')
        return Cipher.decode(plaintext, key)

    def encode(string, key, encode=True):
        originalkey = key
        while len(key) < len(string):
          key = key + originalkey
        out = ""
        for i, c in enumerate(string):
          try: [alphabet.index(c), alphabet.index(key[i])]
          except ValueError: raise NotImplementedError("That character (" + c + ") is not supported")
          # we know that c exists in the alphabet
          out += Cipher.shiftChar(c, alphabet.index(key[i]) if encode else 0 - alphabet.index(key[i]))
        return out

    def decode(string, key):
        return Cipher.encode(string, key, False)

    def shiftChar(c, amount): return alphabet[(alphabet.index(c) + amount) % len(alphabet)]
if __name__ == '__main__':
    print (doctest.testmod())