def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    l1=len(s1)
    l2=len(s2)
    index=0   
    st = ''
    while index < l1+l2 :
        if index < l1:
            st= st + s1[index]
        if index < l2: 
            st = st + s2[index]
        index += 1
    print (st)        

laceStrings('123','1234567')
        