import sys

f = open(sys.argv[1],'r')

for line in f:
    num = int(line.strip())
    if num%2 == 0:
        print 1
    else:
        print 0
    
f.close()    