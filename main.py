import ciphers
import jw_utils
activatedCiphers = [
    ciphers.ceasar.Cipher,
    ciphers.vernam.Cipher
    ]
menu = jw_utils.menu.Menu("Ciphers")

for cipher in activatedCiphers:
    def option():
        secondaryMenu = jw_utils.menu.Menu("\nEncode or decode?")
        def enc():
            print(cipher.encodeFriendly() + "\n")
        def dec():
            print(cipher.decodeFriendly() + "\n")
        secondaryMenu.addOption("Encode", enc)
        secondaryMenu.addOption("Decode", dec)
        def e():
            secondaryMenu.endOptionLoop()
        secondaryMenu.addOption("Exit to cipher selection", e, False)
        secondaryMenu.doMenu()
    menu.addOption(cipher.name, option, False)

menu.doMenu()
