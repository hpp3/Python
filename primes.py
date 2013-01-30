#finding primes

from math import *



def isprime(i):
    for j in range (2,int(sqrt(i))+1):
        if ((i%j) is 0):
            return False
    return True


def getprimes(n):
    p = []
    for i in range(2,n+1):
        if isprime(i):
            p.append(i)
    return p


def main():
    numbers = [True for i in range(n)]
    primes = []
    j = 2
    numbers[0] = False
    sn = int(sqrt(n))
    while j<=sn:
        i = j
        while i*j<=n:
            numbers[i*j-1] = False
            i+=1
        j+=1
    for it, num in enumerate(numbers):
        if num:
            primes.append(it+1)
    return primes

