#!/usr/bin/python
# -*- coding: utf-8 -*-
import doctest
import base64


class Cipher:

    name = 'Vernam Cipher'
    desc = 'Also known as the xor cipher'

    def encodeFriendly():
        plaintext = input(' Text to encode > ')
        key = input(' Key > ')
        return Cipher.encode(plaintext, key)

    def decodeFriendly():
        plaintext = input(' Ciphertext to decode > ')
        key = input(' Key > ')
        return Cipher.decode(plaintext, key)

    def encode(string, key):
        plainTextOctets = [format(x, 'b').rjust(8).replace(' ', '0')# This makes keyOctets an array with len(key) elements,
                           for x in [ord(x) for x in string]]       # where each element is an 8-long string containing a 
                                                                    # binary representation of the unicode character of the key
        keyOctets = [format(x, 'b').rjust(8).replace(' ', '0') for x in # This makes keyOctets an array with len(key) elements,
                     [ord(x) for x in key]]                             # where each element is an 8-long string containing a 
                                                                        # binary representation of the unicode character of the key
        while len(keyOctets) < len(plainTextOctets): # This takes the key and repeats it until 
            for octet in keyOctets:                   #  the key is longer than the plaintext
                if len(keyOctets) > len(plainTextOctets):
                    break
                keyOctets = keyOctets + [octet]
        xorCompleteOctets = [''.join([('1' if Cipher.xor(ptDigit, # This cluster**** of code will
                             keyOctets[i][j]) else '0') for (j, # take an array of plaintext encoded
                             ptDigit) in enumerate(ptOctet)]) for (i, # into binary and xor it against an
                             ptOctet) in enumerate(plainTextOctets)] # array (keyOctets) that is longer than the
        xorCompleteInts = [int(x, base=2) for x in xorCompleteOctets] # plaintext with each element a string of
        xorCompleteHex = [format(k, 'x') for k in xorCompleteInts] # length 8 with a binary encoded integer
        xorCompleteB64 = \
            base64.b85encode(bytes(' '.join(xorCompleteHex), 'utf-8')) # Converts the hex encoded encrypted input into base85 for compactness
        return xorCompleteB64.decode('utf-8')

    def decode(string, key):

        xorCompleteHex = base64.b85decode(string.encode('utf-8'
                )).decode('utf-8').split(' ')
        xorCompleteInts = [int(x, base=16) for x in xorCompleteHex]
        xorCompleteOctets = [format(x, 'b').rjust(8).replace(' ', '0')
                             for x in xorCompleteInts]
        keyOctets = [format(x, 'b').rjust(8).replace(' ', '0') for x in
                     [ord(x) for x in key]]

        while len(keyOctets) < len(xorCompleteOctets):
            for octet in keyOctets:
                if len(keyOctets) > len(xorCompleteOctets):
                    break
                keyOctets = keyOctets + [octet]
        plainTextOctets = [''.join([('1' if Cipher.xor(cipherDigit,
                           keyOctets[i][j]) else '0') for (j,
                           cipherDigit) in enumerate(cipherOctet)])
                           for (i, cipherOctet) in
                           enumerate(xorCompleteOctets)]
        plainTextInts = [int(x, base=2) for x in plainTextOctets]
        plainTextChars = [chr(x) for x in plainTextInts]
        plainText = ''.join(plainTextChars)
        return plainText

    def xor(a, b):
        """
        >>> Cipher.xor("0", "0")
        False

        >>> Cipher.xor("1", "0")
        True

        >>> Cipher.xor("0", "1")
        True

        >>> Cipher.xor("1", "1")
        False
        """

        return bool(int(a) ^ int(b))


if __name__ == '__main__':
    print (doctest.testmod())

			
