def isPrime(num):
    flag = True
    for k in range(2,num):
        if (num%k) == 0:
            flag = False
    return flag

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

num=1000

while num>2:
    if isPrime(num):
        if isPal(str(num)):
            print num     
            break 
    num=num-1  
