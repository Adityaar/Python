def selectionsort(alist):    

    l = len(alist)    
    for passnum in range(l-1,0,-1):        
        pos = 0
        for i in range(1,passnum+1):
            if alist[i] > alist[pos] :
                pos = i
        temp = alist[passnum]
        alist[passnum] = alist[pos]
        alist[pos] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionsort(alist)
print(alist)
                