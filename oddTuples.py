def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    cnt=1
    oddT = ()
    for a in aTup:
        if cnt%2==1:
            oddT = oddT +(a,)
        cnt += 1
    return oddT

a=('I', 'am', 'a', 'test', 'tuple')        
print oddTuples(a)
