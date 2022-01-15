import random
from sort_utils import selection_sort

SZ = 10

for i in range(100):
    L = [random.randint(0,2*SZ) for i in range(SZ)]
    print('init',L)
    rL = selection_sort(L[:])
    
    if sorted(L) != rL:
        print(i)
        print(L[:10])
        print(rL[:10])
