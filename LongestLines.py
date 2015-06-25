import sys

input_file=open(sys.argv[1], 'r')
myDict={}

num_lines=int(input_file.readline())


for line in input_file:
    myDict[len(line.strip())]=line.strip()

sortedKeys=sorted(myDict.keys(),reverse=True)

for i in range(num_lines):
    print myDict[sortedKeys[i]]

       
def bubbleSort(alist):
    for j in range(len(alist)):
        for i in range(len(alist)-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

