import sys
import os

input_file = open(sys.argv[1], 'r')

sum=0
for lines in input_file:
    sum = sum + int(lines.strip())
print sum
print os.path.getsize(sys.argv[1])