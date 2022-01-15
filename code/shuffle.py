import random

def run_length():
    rL = [4,3,3,2,2,1,1]
    return random.choice(rL)

def one_shuffle(L):
    rL = list()
    n = int(len(L)/2)
    L1 = L[:n]
    L2 = L[n:]
    
    # make sure top card switches
    if random.randint(0,1) == 0:
        L1,L2 = L2,L1
    
    while True:
        i = run_length()
        rL.extend(L1[:i])
        L1 = L1[i:]
        
        j = run_length()
        rL.extend(L2[:j])
        L2 = L2[j:]
        
        # if we're out of cards in one hand
        if not L1:
            if L2:
               rL.extend(L2)
            break
        if not L2:
            if L1:
                rL.extend(L1)
            break
    return rL

L = list('AKQJT9876')
t = ' '.join(L)

for i in range(int(1e7)):
    L = one_shuffle(L)
    u = ' '.join(L)
    if u == t:
        print(i)
        print(t)
        break

'''
> p3 shuffle.py
529371
A K Q J T 9 8 7 6
> p3 shuffle.py
976018
A K Q J T 9 8 7 6
> p3 shuffle.py
549556
A K Q J T 9 8 7 6
> p3 shuffle.py
427895
A K Q J T 9 8 7 6
> p3 shuffle.py
126396
A K Q J T 9 8 7 6
> p3 shuffle.py
9126
A K Q J T 9 8 7 6
> p3 shuffle.py
525548
A K Q J T 9 8 7 6
> 
'''