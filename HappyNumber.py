import sys

'''
 A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, 
 and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
 Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

For the curious, here's why 7 is a happy number: 7->49->97->130->10->1. 
Here's why 22 is NOT a happy number: 22->8->64->52->29->85->89->145->42->20->4->16->37->58->89 ... 

Input sample:
=============
The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. E.g. 

1
7
22

Output sample:
==============
If the number is a happy number, print out 1. 
If not, print out 0. E.g 

'''
def sumSquares(n):
    st=str(n)
    sum=0
    for i in range(len(st)):
        sum = sum + int(st[i])*int(st[i])
    return sum

def isHappy(n):
    try:
        val=sumSquares(n)
        #print val
        if val == 1:
            return 1
        else:
            return isHappy(val)
    except RuntimeError:
        return 0
#print sumSquares(7)
#print sumSquares(49)
#print sumSquares(97)   
#print sumSquares(130) 
#print isHappy(7)
        
f = open(sys.argv[1],'r')

for lines in f:
    num = int(lines.strip())
    print isHappy(num)    