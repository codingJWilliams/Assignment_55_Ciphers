import ciphers
import jw_utils
import sys
try: colorInternal = sys.stdout.shell.write
except AttributeError: raise RuntimeError("Use IDLE")
colorDef = {
  "red": "stderr",
  "black": "stdin",
  "purple": "BUILTIN",
  "green": "STRING",
  "dark_red": "console",
  "blue": "stdout",
  "orange": "KEYWORD",
  "white_on_black": "hit",
  "black_on_red": "ERROR"
}
activatedCiphers = [
    ciphers.ceasar.Cipher,
    ciphers.vernam.Cipher,
    ciphers.vigenere.Cipher
    ]
menu = jw_utils.menu.Menu("Ciphers")

for cipher in activatedCiphers:
    def option(cipher=cipher): # cipher=cipher is a shim to allow defining in loop
        secondaryMenu = jw_utils.menu.Menu("\nEncode or decode? (" + cipher.name + ")")
        def enc():
            out = cipher.encodeFriendly()
            colorInternal("Ciphertext: ", colorDef["green"])
            colorInternal(out + "\n", colorDef["red"])
        def dec():
            out = cipher.decodeFriendly()
            colorInternal("Plaintext: ", colorDef["green"])
            colorInternal(out + "\n", colorDef["black"])
        secondaryMenu.addOption("Encode", enc)
        secondaryMenu.addOption("Decode", dec)
        def e():
            secondaryMenu.endOptionLoop()
        secondaryMenu.addOption("Exit to cipher selection", e, False)
        secondaryMenu.doMenu()
    menu.addOption(cipher.name, option, False)

menu.doMenu()
