import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    #print fib(int(test))
    a, b = test.split(',')
    x = int(a)
    n = int(b)
            
    for i in range(x):
        if i*n>= x:
            break
    print i*n
test_cases.close()
