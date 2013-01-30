#converts all integers in a list (recursively) into hexidecimal

def hexprint(l):
	f = []
	if l.__class__() == []:
		print "[",
		for item in l:
			hexprint(item)
		print "]",
	else:
		if l.__class__() == 0:
			print "%x" % l,
		else:
			print l,

crazy = [11, 25, [23, 36, "string"], [22, 31, [62, 21], 0], "rofl"]

hexprint(crazy)
