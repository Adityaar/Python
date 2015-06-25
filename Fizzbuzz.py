import sys

f = open(sys.argv[1],'r')

for line in f:
    in_line = line.strip().split()
    X = int(in_line[0])
    Y = int(in_line[1])
    n = int(in_line[2])
        
    lst = []
    for i in range(1,n+1):
        if i%X == 0 :
            if i%Y == 0:
                lst.append('FB')
            else:
                lst.append('F')
        elif i%Y == 0:
            lst.append('B')
        else:
            lst.append(i)
    for x in lst:
        print x,
    print
f.close()
