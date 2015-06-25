def McNuggets(n):
    """
    n is an int
    
    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
 
    '''if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
    return False
    '''
    
    for a in range(0,n):
        for b in range(0,n):
            for c in range(0,n):
                if 6*a+9*b+20*c == n:
                    return True
    return False            