import sys

fn = 'words5.txt'
p = '/Users/telliott/Dropbox/Github/Python3 Intro/data/'
with open(p+fn) as fh:
    data = fh.read()
L = data.strip().split('\n')

#-----

t = sys.argv[1]
g = []
b = []

for i,arg in enumerate(sys.argv):
    if arg == '-g':
        g = list(sys.argv[i+1])
    elif arg == '-b':
        b = list(sys.argv[i+1])

#-----

def test(word,t):
    for x in word:
        if x in b:
            return
    for y in g:
        if not y in word:
            return
    for x,y in zip(word,t):
        if y == '.':
            continue
        if x != y:
            return
    return word

pL = []
for word in L:
    if len(word) == len(t):
        match = test(word,t)
        if match:
            pL.append(match)
      
N = len(pL)      
print(N)
for word in pL[:20]:
    print(word)