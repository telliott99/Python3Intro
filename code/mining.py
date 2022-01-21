import sys, hashlib, time 

data = sys.argv[1]
t = '0' * int(sys.argv[2])

def one_run():
    start = time.time()
    m = hashlib.md5()
    m.update(data.encode('UTF-8'))
    i = 0
    while True:
        i += 1
        c = m.copy()
        c.update(str(i).encode('UTF-8'))
        h = str(c.hexdigest())
        if h.startswith(t):
            x = '%10.4f' % (time.time() - start)
            s = str(i).rjust(10)
            print(x,s,h[:20] + '...')
            break

one_run()