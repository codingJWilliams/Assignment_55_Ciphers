
def alignComments(fileName, cols=100):
  with open(fileName, "r") as f:
    fContent = f.read().splitlines()
  temp = []
  for a in fContent: temp += [ a.replace("\n", "") ]
