import sys

f = open(sys.argv[1],'r')

def isPrime(num):
    flag = True
    for k in range(2,num):
        if (num%k) == 0:
            flag = False
    return flag

for line in f:
    [low,high] = line.strip().split(',')
    cnt = 0
    l = int(low)
    h = int(high)
    for n in range(l,h+1):
        if isPrime(n):
           cnt += 1
    print cnt

f.close()