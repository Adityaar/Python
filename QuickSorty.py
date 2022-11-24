""" Quick sort Algo to sort a random list of numbers. """
def quickSort(alist):
    """ A wrapper function for first call to recursive quick Sort function"""
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    """ A recursive function that uses a divide and conquer strategy to partition the array(problem)
        into sub-arrays(sub-problems) and Solve the sub-problems.
        Then, there is no need for combining the solutions.
    """
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    """ Partition the input array(problem) into two using a Pivot(or dividing element) such that
        after the completion of the process, all elements in first set are less than the pivot
        and all elements in second set are greater than the Pivot.
        Return the final position of the pivot element.
        Current implementation starts by choosing the First element of the array as the pivot.
        We are free to choose any element as the Pivot.
        Some of the other approaches are:
        a. Examine the first, last and middle items of the input array. Use the value that is
        between the other two for the dividing item.
        b. Pick a random index from the input array to sort and then use the value at that
        index as the Pivot/Dividing item.
    """
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            (alist[first] , alist[rightmark]) = (alist[rightmark] , alist[first])
    return rightmark

unordered_list = [54,26,93,17,77,31,44,55,20]
ordered_list = quickSort(unordered_list)
print(ordered_list)
