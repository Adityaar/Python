import sys

f = open(sys.argv[1],'r')

for line in f:
    words = line.strip().split();
    for word in words:
        print word[0].upper() + word[1:] ,
    print