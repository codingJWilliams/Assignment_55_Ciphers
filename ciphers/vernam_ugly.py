import doctest, base64

class Cipher:
    name = "Vernam Cipher"
    desc = "Also known as the xor cipher"
    def encodeFriendly():
        plaintext = input(" Text to encode > ")
        key = input(" Key > ")
        return Cipher.encode(plaintext, key)
    def decodeFriendly():
        plaintext = input(" Ciphertext to decode > ")
        key = input(" Key > ")
        return Cipher.decode(plaintext, key)
    #def encode(string, key):
    #    binaryInput = ' '.join('{0:08b}'.format(ord(x), 'b') for x in string)
    #    binaryKey = ' '.join('{0:08b}'.format(ord(x), 'b') for x in key)
    #    while len(binaryInput) > len(binaryKey):
    #        binaryKey = binaryKey * 2
    #    return "".join([x.replace("0x", "") + " " for x in [hex(int(x, 2)) for x in "".join([str(x) for x in [1 if x and x != " " else 0 if x != " " else " " for x in [Cipher.xor(i,list(binaryKey)[x]) if i != " " else " " for x,i in enumerate(binaryInput)]]]).split(" ")]])
    def encode(string,key):
        plainTextOctets = [
            format(x, 'b').rjust(8).replace(" ", "0")
            for x in [
                ord(x) for x in string
                ]
            ]
        keyOctets = [
            format(x, 'b').rjust(8).replace(" ", "0")
            for x in [
                ord(x) for x in key
                ]
            ]
        while len(keyOctets) < len(plainTextOctets):
            for octet in keyOctets:
                if len(keyOctets) > len(plainTextOctets): break
                keyOctets = keyOctets + [octet]
        xorCompleteOctets = [
            "".join([
                "1" if Cipher.xor(ptDigit, keyOctets[i][j]) else "0"
                for j, ptDigit in enumerate(ptOctet)
                ])
            for i, ptOctet in enumerate(plainTextOctets)
            ]
        xorCompleteInts = [
            int(x, base=2)
            for x in xorCompleteOctets
            ]
        xorCompleteHex = [
            format(k, 'x')
            for k in xorCompleteInts
            ]
        xorCompleteB64 = base64.b85encode(bytes(" ".join(xorCompleteHex), "utf-8"))            
        return xorCompleteB64.decode("utf-8")
    def decode(string, key):
        
                
        xorCompleteHex = base64.b85decode(string.encode("utf-8")).decode("utf-8").split(" ")
        xorCompleteInts = [
            int(x, base=16)
            for x in xorCompleteHex
            ]
        xorCompleteOctets = [
            format(x, 'b').rjust(8).replace(" ", "0")
            for x in xorCompleteInts
            ]
        keyOctets = [
            format(x, 'b').rjust(8).replace(" ", "0")
            for x in [
                ord(x) for x in key
                ]
            ]
        while len(keyOctets) < len(xorCompleteOctets):
            for octet in keyOctets:
                if len(keyOctets) > len(xorCompleteOctets): break
                keyOctets = keyOctets + [octet]
        plainTextOctets = [
            "".join([
                "1" if Cipher.xor(cipherDigit, keyOctets[i][j]) else "0"
                for j, cipherDigit in enumerate(cipherOctet)
                ])
            for i, cipherOctet in enumerate(xorCompleteOctets)
            ]
        plainTextInts = [int(x, base=2) for x in plainTextOctets]
        plainTextChars = [chr(x) for x in plainTextInts]
        plainText = "".join(plainTextChars)
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
if __name__ == "__main__":
    print(doctest.testmod())
