def isPrime(num):
    flag = True
    for k in range(2,num):
        if (num%k) == 0:
            flag = False
    return flag
       
    
#primes=[]
total=0
i=1
num=2
while i <= 1000:
    if isPrime(num):
        #primes.append(num)
        total=total+num
        i = i+1
    num=num+1
print str(total)