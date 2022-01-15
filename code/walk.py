import random
import matplotlib.pyplot as plt

random.seed(1331)

X = range(10000)
colors = list('bgrcmk')

for c in colors:
    pos = 0
    L = [pos]
    for x in X[1:]:
        pos += random.choice((-1,1))
        L.append(pos)
    plt.plot(X,L,color=c)

plt.savefig('walk.png')
