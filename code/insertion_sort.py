import random

N = 100
R = range(16)

def handle_insertion(i,j,L):
    if i != j:    
        L = L[:j] + [L[i]] + L[j:i] + L[i+1:] 
    return L

def find_insertion_point(i,L):
    value = L[i]
    for j in range(i):
        if value < L[j]:
            return j
    return i

def run():
    L = [random.randint(0,N) for i in R]
    for i in R:
        j = find_insertion_point(i,L)
        L = handle_insertion(i,j,L)      
    print(L)
    assert sorted(L) == L
    
for c in range(100):
    run()
            
