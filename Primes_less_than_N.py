import sys

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num%2 == 0:
        return False
        
    for k in range(3,int(num**0.5)+1, 2):
        if (num%k) == 0:
            return False
    return True

test_cases = open(sys.argv[1], 'r')
for num in test_cases:
    if num > 2:
        primes=[]
        for k in range(1,int(num)):
            if isPrime(k):
                primes.append(k)
    else:
        primes.append(0)
    print ",".join(str(x) for x in primes)
    
            