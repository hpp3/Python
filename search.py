#implementation of binary search and search using golden ratio

from math import *

def binarysearch(array, query):
    div = int(round(len(array)*0.5))-1
    if array[div] == query:
        return div
    if array[div] < query:
        return goldensearch(array[div+1:],query)+div+1
    else:
        return goldensearch(array[:div],query)
    
def goldensearch(array, query):
    div = int(round(len(array)*0.618))-1
    if array[div] == query:
        return div
    if array[div] < query:
        return goldensearch(array[div+1:],query)+div+1
    else:
        return goldensearch(array[:div],query)
