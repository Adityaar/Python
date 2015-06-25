import sys

'''
 Write a program which finds the first non-repeated character in a string.

The first argument is a path to a file. The file contains strings.

For example:

Input sample:
------------
yellow
tooth

Output sample:

Print to stdout the first non-repeated character, one per line.

For example:
------------
y
h

'''
f = open(sys.argv[1],'r')

for line in f:
    st = line.strip()
    aDict = {}
    lst = []
    for ch in st:
        try:
            aDict[ch] += 1
        except:
            aDict[ch] = 1
            lst.append(ch)

    for key in lst:
        if aDict[key] == 1:
            print key
            break

    
    