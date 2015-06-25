def insertionsort(alist):
    for index in range(1,len(alist)):
        
        currval = alist[index]
        pos = index
        
        while alist[index-1] > currval and pos >0:
            alist[pos] = alist[pos-1]
            pos = pos - 1
        
        alist[pos] = currval


alist = [54,26,93,17,77,31,44,55,20]
insertionsort(alist)
print(alist)
        