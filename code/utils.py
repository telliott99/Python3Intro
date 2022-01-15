def minme(L):
    # return the minimum int of a list
    # some (all) values may be None
    ret = -1
    index = -1
    
    #print(L)
    for i,n in enumerate(L):
        if n is None:
            continue
            
        if ret == -1 or n < ret:
            ret = n
            index = i
            
    if ret == None:
        return None
    
    # print(index,ret)
    return index,ret

if __name__ == "__main__":
    print(minme([10,None,1]))