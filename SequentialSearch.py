def sequentialSearch(alist,item):
    found=False
    
    for i in alist:
        if item == i:
            found = True
            break
    return found

def orderedSequentialSearch(alist,item):
    loop=0
    found = False
    for i in alist:
        loop += 1
        if item == i:
            found = True
            break
        elif i > item:
            break
    print "number of comparisons:" + str(loop)        
            
    return found

        
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print(sequentialSearch(testlist, 3))        
print(sequentialSearch(testlist, 13))

testlist1 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist1, 3))
print(orderedSequentialSearch(testlist1, 13))
