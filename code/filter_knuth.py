import operator

p = '/Users/telliott/Dropbox/'
p += 'Github/Python3Intro/data/'

# https://norvig.com/ngrams/
# words with frequency counts
fn = p + "count_1w.txt"
with open(fn) as fh:
    data = fh.read()
norvig = data.strip().split('\n')

D = dict()
for e in norvig:
    w,count = e.strip().split()
    if len(w) == 5:
        D[w] = count

fn = p + 'sgb-words.txt'
with open(fn) as fh:
    data = fh.read()
knuth = data.strip().split('\n')

L = list()
discard = list()

for w in knuth:
    if w in D:
        count = D[w]
        L.append((w,int(count)))

# print(len(L),len(discard))
# 5215 542

L.sort(key=operator.itemgetter(1)) # by count
L.reverse()
for w,count in L:
    print(w)

