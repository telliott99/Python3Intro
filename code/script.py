import sys, random
random.seed(151)
from sorting_methods import selection_sort

SZ = 10
L = [random.randint(0,100) for i in range(SZ)]
print(L)
rL = selection_sort(L)
print(rL)