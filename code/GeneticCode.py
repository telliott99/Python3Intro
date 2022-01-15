def get_GC_dict():

    aaL = ['FFLLSSSSYY**CC*W',
           'LLLLPPPPHHEERRRR',
           'IIIMTTTTNNKKSSRR',
           'VVVVAAAADDEEGGGG']
    
    aa = ''.join(aaL)  
        
    s = 'UCAG'
    codons = [x+y+z for x in s for y in s for z in s]
    return dict(zip(codons,list(aa)))
