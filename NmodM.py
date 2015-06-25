import sys

f = open(sys.argv[1],'r')

for line in f:
    [a,b] = line.strip().split(',');
    n = int(a)
    m = int(b)
    
    if n>m:        
        while True:
            #print n , 
            if n - m >= 0:
                #cnt += 1
                n = n - m
            else:
                break
        print n
    elif n == m:
        print 0
    else:
        print n

    
             