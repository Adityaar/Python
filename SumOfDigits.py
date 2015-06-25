import sys

input_file=open(sys.argv[1], 'r')

numbers=input_file.readlines()

for num in numbers:
    sum = 0
    st = str(num).strip()
    for i in range(len(st)):
        #print i, st[i]
        sum = sum + int(st[i])
    print sum
    