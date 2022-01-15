import sys
from utils import minme

def selection_sort(input):
    L = input[:]
    rL = list()
    
    while True:
        result = minme(L)
        if not result:
            break
        i,v = result
        #print(i,v)
        L[i] = None
        rL.append(v)
        
    return rL

