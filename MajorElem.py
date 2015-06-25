import sys

'''
Challenge Description:

The major element in a sequence with the length of L is the element which appears in a sequence more than L/2 times. The challenge is to find that element in a sequence.
Input sample:

Your program should accept as its first argument a path to a filename. Each line of the file contains a sequence of integers N separated by comma. E.g. 

92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19
92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92
4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42

Output:
=======
For each sequence print out the major element or print "None" in case there is no such element. E.g. 

19
92
None
'''

f = open(sys.argv[1],'r')

for line in f:
    numFreq = {}
    nums = line.strip().split(',')
    L = len(nums)
    found = False
    
    for n in nums:
        try:
            numFreq[n] += 1
        except:     
            numFreq[n] = 1

    for k in numFreq.keys():
        if numFreq[k] > L/2 :
            print k
            found = True
            break            

    if not found:
        print "None"
                                                   