import sys

f = open(sys.argv[1],'r')
           
for line in f:
    [s1,s2]=line.strip().split(';')
    common=[]
    for i in s1.split(','):
        for j in s2.split(','):
            if i==j:
                common.append(i)    
    print ','.join(common)
        