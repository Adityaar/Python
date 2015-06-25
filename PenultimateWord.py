import sys

f = open(sys.argv[1],'r')

for line in f:
    wordList = line.strip().split()
    print wordList[len(wordList)-2]

f.close()        
