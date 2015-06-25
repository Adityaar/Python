import sys

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print fib(int(test))
test_cases.close()
