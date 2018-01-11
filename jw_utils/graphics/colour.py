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

def multiColor(colorArr):
  for item in colorArr:
    colorInternal(item[0], colorDef[item[1]])
  colorInternal("\n", "stdout")
