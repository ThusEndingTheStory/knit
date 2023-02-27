from sys import argv

def err(msg):
  print("Knit: Error: " + msg)
  exit(1)

def o():
  try:
    return open(argv[1], "r").readlines()
  except:
    err("Couldn't open target file")
    
print(o())
