def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    elif exp%2==0:
        return recurPower(base*base,(exp)/2)
    else:
        return base * recurPower(base,exp-1)
print recurPower(3,3)        