#Finds all one word anagram groups in the English language

from math import *
def invert_dict(d):
    inv = {}
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val]= [key]
        else:
            inv[val].append(key)
    return inv

def order(a):
    l = list(a)
    l.sort()
    w = ''
    l = w.join(l)
    return l

def print_dict(d):
	for key in d:
		print key, "=>", d[key]	
	
def anagram(x = 0):
	fin = open('words.txt')
	d = {}
	for line in fin:
		word = line.strip()
		l = order(word)
		if l not in d: 
			d[l] = [word]
		else:
			d[l].append(word)
	d2 = {}
	d3 = {}
	for key in d:
		if len(d[key]) > 1:
			d2[key] = d[key]
			d3[key] = len(d[key])

	d4 = invert_dict(d3)
	d5 = list(d4)
	d5.sort()
	d5.reverse()
	if x == 0:
		for num in d5:
			for key in d4[num]:
				print d2[key]
	else:
		a=order(x)
		print d2[a]
		
anagram()
