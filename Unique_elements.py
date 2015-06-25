'''
You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

Input sample:
=============
File containing a list of sorted integers, comma delimited, one per line. E.g. 

1,1,1,2,2,3,3,4,4
2,3,4,5,5

Output:
=======
1,2,3,4
2,3,4,5
    
'''
import sys

f = open(sys.argv[1],'r')
for line in f:
    t=[]
    l=line.strip().split(',')
    #print l
    for i in range(len(l)):
        #aDict[l[i]]=1
        #prev=l[i]
        if i == 0:
            t.append(l[i])
            prev = l[i]
        elif i !=0 and l[i]==prev:
            pass
        else:
            t.append(l[i])
            prev = l[i]
    print ','.join(t)