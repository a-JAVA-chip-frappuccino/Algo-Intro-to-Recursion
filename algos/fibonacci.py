'''

iterative algorithm

'''

def fib_iter(n):
    first = 0
    second = 1

    if n == 1:
        return first
    elif n == 2:
        return second
    
    for i in range(3, n + 1):
        temp_second = second

        second = second + first
        first = temp_second

    return second

fibonacci = fib_iter(1)

print(fibonacci)

'''

recursive algorithm

'''

def fib_recur(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recur(n - 2) + fib_recur(n - 1)
    
fibonacci = fib_recur(40)

print(fibonacci)