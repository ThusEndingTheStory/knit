from sys import argv
from os import system

strings = {}
integers = {}

def err(msg):
	# system('clear')
	print("Knit: Error: " + msg)
	exit(1)

def run(file):
	lineNum = 0
	for line in file:
		lineNum += 1
		words = line.split(";")
		l = len(words)
		# Empty line handling
		if l == 0:
			pass
		# Echo
		elif l == 2 and words[0] == "echo":
			if words[1][:-1] in strings:
				print(strings[words[1][:-1]])
			elif words[1][:-1] in integers:
				print(integers[words[1][:-1]])
			else:
				print(words[1], end="")
		# Strings
		elif l == 3 and words[1] == "str":
			strings[words[0]] = words[2][:-1]
		# Integers
		elif l == 3 and words[1] == "int" and words[2][:-1].isdigit():
			integers[words[0]] = float(words[2][:-1])
		# Integer Mutation
		elif l == 4 and words[0] == "mut" and words[3][:-1].isdigit() and words[1] in integers:
			if words[2] == "+":
				print("+")
				integers[words[1]] += float(words[3][:-1])
			elif words[2] == "-":
				print("-")
				integers[words[1]] -= float(words[3][:-1])
			elif words[2] == "*":
				print("*")
				integers[words[1]] *= float(words[3][:-1])
			elif words[2] == "/":
				print("/")
				integers[words[1]] /= float(words[3][:-1])
		# String Mutation
		elif l == 3 and words[0] == "mut" and words[1] in strings:
			strings[words[1]] += words[2][:-1]
			
def o():
	# try:
		f = open(argv[1], "r").readlines()
		i = 0
		while i < len(f)-1:
			i += 1
		# print("The thingy:" + f[i][len(f[i]):] + ":")
		# print("The other thingy:" + f[i][len(f[i])-1:] + ":")
		# print("length f[i] or something: " + str(len(f[i])-1))
		if f[i][len(f[i])-1:] != "\n":
			f[i] += "\n"
		return f
	# except:
	# 	err("Couldn't open target file")
    
run(o())
# print(el())
