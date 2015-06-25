import sys

test_cases = open(sys.argv[1], 'r')

for lines in test_cases:
    print lines.lower()

test_cases.close()        