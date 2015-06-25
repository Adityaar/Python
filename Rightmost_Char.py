import sys

f = open(sys.argv[1],'r')
           
for line in f:
    [st,ch]=line.strip().split(',')
    key=0
    for i in range(len(st)):
        if st[i] == ch:
            key=i    
    if key==0:
        print "-1"
    else:
        print key
f.close()        
                