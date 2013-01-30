#randomly walks through directory system

import os
cwd = os.getcwd()

def walk(dir):
	l = []
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			l.append(path)
		else:
			walk(path)
	print l

walk(cwd)
