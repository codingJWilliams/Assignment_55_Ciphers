import doctest

class Cipher:
    name = "Ceasar Cipher"
    desc = "Shifts a character by it's ascii value"
    def encodeFriendly():
        plaintext = input(" Text to encode > ")
        inp = input(" Shift [13] > ")
        shift = int(inp) if len(inp) else 13
        return Cipher.encode(plaintext, shift)
    def decodeFriendly():
        plaintext = input(" Ciphertext to decode > ")
        inp = input(" Shift [13] > ")
        shift = inp if len(inp) else 13
        return Cipher.decode(plaintext, shift)
    def encode(string, shift=13):
        OUT = ""
        for c in string:
            asciiPoint = ord(c) + shift
            if (asciiPoint > 126): asciiPoint = (asciiPoint % 126) + 32
            OUT += chr(asciiPoint)
        return OUT
    def decode(string, shift=13):
        OUT = ""
        for c in string:
            asciiPoint = ord(c) - shift
            if (asciiPoint < 32): asciiPoint = asciiPoint + 94
            OUT += chr(asciiPoint)
        return OUT
