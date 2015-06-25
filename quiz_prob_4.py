def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x < b:
        return 0
    p = 1
    val=b
    while (val<x):
        if val*b > x:
            return p
        p +=1
        val = recPow(p,b)            
    return p
    
def recPow(n,base):
    if n==0:
        return 1
    elif n==1:
        return base
    else:
        return recPow(n-1,base) * base
    