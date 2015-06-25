import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    words = test.split()
    words.reverse()
    print ' '.join(words)

test_cases.close()
