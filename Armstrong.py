import sys

f = open(sys.argv[1],'r')

for line in f:
    num = line.strip()
    p = len(num)
    Sum = 0
    for i in num:
        Sum = Sum + int(i) ** p
    if Sum == int(num):
        print 'True'
    else:
        print 'False'    
            
f.close()    
    