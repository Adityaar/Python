
def bubbleSort(alist):
    for j in range(len(alist)):
        for i in range(len(alist)-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
            
alist = [54,26,93,17,77,31,44,55,20]
print(alist)
bubbleSort(alist)
print(alist)

