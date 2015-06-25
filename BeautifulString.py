import sys

f = open(sys.argv[1],'r')

for line in f:
    aDict = {}
    beauty = 0
    n = 26
    st = line.strip().upper()
    
    for ch in st:        
        if ch.isalpha() :
            try:
                aDict[ch] += 1
            except:
                aDict[ch] = 1
    
    for w in sorted(aDict, key=aDict.get, reverse=True):
        
        beauty = beauty + aDict[w] * n
        n = n-1
    print beauty
        
f.close()
