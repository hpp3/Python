# a collection of functions mostly related to strings and dictionaries
import string

from math import *
def has_no_e():
    word = raw_input('Type a word: ')
    for letter in word:
        if letter == 'e':
            return True
    return False

def words():
    fin = open('words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        print word
def no_e_words():
    fin = open('words.txt')
    line = fin.readline()
    count = 0
    count2 = 0
    for line in fin:
        word = line.strip()
        count2 = count2 +1
        if 'e' not in word:
            if count%100 == 0:
                print word
            count = count +1
    print count
    print count2
    print '%', count*1.0/count2*100.0

def avoids(word, string):
    if string not in word:
        print 'True'
        return True
    print 'False'
    return False

def myavoids():
    while True: 
        fin = open('words.txt')
        count = 0
        string = raw_input('Enter a forbidden string\n')
        print "input: ", string
        if string == 'Done':
            break
        for line in fin:
            word = line.strip()
            if string in word:
                count = count +1
        print 'count: ', count
        fin.close()


def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True

def palindrome():
    fin = open('words.txt')
    line = fin.readline()
    count = 0
    count2 = 0
    for line in fin:
        word = line.strip()
        count2 = count2 +1
        if is_palindrome(word)==True:
            print word
            count = count +1
    print 'Palindrome', count
    print 'Total', count2
    print '%', count*1.0/count2*100.0


def is_hex(word):
    for letter in word:
        if letter not in 'abcdefoli':
            return False
    return True


def hexidecimal():
    fin = open('words.txt')
    line = fin.readline()
    count = 0
    count2 = 0
    for line in fin:
        word = line.strip()
        count2 = count2 +1
        if is_hex(word)==True:
            print word
            count = count +1
    print 'Hex', count
    print 'Total', count2
    print '%', count*1.0/count2*100.0

def cumulat(var):
    res = []
    prev=0
    for cur in var:
        term = cur+prev
        prev = term
        res.append(term)
        
    return res


def is_palin(x):
    y=list(x)
    y.reverse()
    delimiter = ''
    y=delimiter.join(y)
    if y == x:
        print 'True'
    else:
        print 'False'

def histogram(s):
    d={}
    for c in s:
        d[c] = d.get(c, 0)+1
    return d

def sortdict(d):
    f = d.keys()
    f.sort()
    for t in f: 
        print t, d[t]

def reverse_lookup(d, v):
    e=[]
    for k in d:
        if d[k] ==v:
            e.append(k)
    print e

def invert_dict(d):
    inv = {}
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val]= [key]
        else:
            inv[val].append(key)
    return inv

def is_anagram(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False


def most_frequent(var):
    e=histogram(var)
    d=invert_dict(e)
    f = d.keys()
    f.sort()
    f.reverse()
    j = 0
    for i in f:
        if j < 3:
            print d[i]
            j += len(d[i])
    print d

def print_dict(d):
	for key in d:
		print "%30s => %d"%(key, d[key])


def most_common(h):
	t=[]
	for key, value in h.items():
		t.append((value,key))
	t.sort()
	t.reverse()
	return t

def lowerfile(x):
	v = {}

	fin = open(x)
	for line in fin:
		line.replace('-', ' ')
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()
			v[word] = v.get(word, 0)+1
	return v

def failure(v):
	a = lowerfile(v)
	b = lowerfile('words.txt')
	for key in a:
		if key not in b:
			print key
 

def commondisplay(v):
	d = most_common(v)
	print "The most common words are:"
	for number, word in d[0:20]:
		print "%30s => %d"%(word, number)
 

