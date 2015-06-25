import sys

'''
 You are given a list of numbers which is supplemented with positions that have to be swapped.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above (2nd line) first you process 0-1, then 1-3.
Output sample:

Print the lists in the following way.

9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10
'''

f = open(sys.argv[1],'r')

for line in f:
    lst = line.strip().split(':')
    swappers = lst[1].strip().split(',')
    num_list = lst[0].split()
    
    for pos in swappers:
        temp = 0
        [pos1,pos2] = pos.strip().split('-') 
           
        temp = num_list[int(pos1)]
        num_list[int(pos1)] = num_list[int(pos2)]
        num_list[int(pos2)] = temp
    for num in num_list:
        print num ,
    print
f.close()    