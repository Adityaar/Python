import sys

f = open(sys.argv[1],'r')

def merge_sort(lst):
    
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left,right)

def merge(lt,rt):
            
    if not lt:
        return rt
    if not rt:
        return lt
    if lt[0] < rt[0]:
        return [lt[0]] + merge(lt[1:],rt)
    else:
        return [rt[0]] + merge(lt,rt[1:])
        
#alist = [54,26,93,17,77,31,44,55,20]
'''
alist1 = [-37.507 ,-3.263, 40.079, 27.999, 65.213, -55.552]
alist2 = [70.920, -38.797, 14.354, 99.323 ,90.374, 7.581]

print merge_sort(alist1)
print merge_sort(alist2)

'''
for line in f:    
    alist = line.strip()
    l= alist.split()
    print l
    #.split()
    t = merge_sort(l)
    print t

#print(alist)


