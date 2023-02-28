from sys import argv

def run(file):
	for line in file:
		words = line.split("*")
		if words[0] == "echo":
			print(words[1])

def err(msg):
	print("Knit: Error: " + msg)
	exit(1)

def o():
	try:
		return open(argv[1], "r").readlines()
	except:
		err("Couldn't open target file")
    
run(o())
