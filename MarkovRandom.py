from words import *
import random

#Generates random passages using Markov analysis of a sample text.
#Sample text must be sufficiently long for best results.

infile = "input.txt"

def next(prefix, word):
	return (prefix[1], word)
def parser():
# parser

	d = {}
	x = 0
	a = ""
	text = open(infile)
	for line in text:
		stripped = line.strip() + " "
		a = a + stripped
	gist = a.split()
	for part in gist[0:-2]:
		if d.get((gist[x], gist[x+1]), 0) == 0:
			d[(gist[x], gist[x+1])] = [gist[x+2]]
		else: 
			d[(gist[x], gist[x+1])].append(gist[x+2])
		x = x+1
	return d

def markov(first, second):
	d = parser()
	prefix = (first, second)
	print first, second,
	for i in range(500):
		word = random.choice(d[prefix])
		print word,
		prefix = next(prefix, word)
		
markov("It", "is")
