'''

iterative algorithm

'''

def exp_iter(base, power):
    exp = 1

    for i in range(power):
        exp = exp * base

    return exp

exponent = exp_iter(5, 3)

print(exponent)

'''

recursive algorithm

'''

def exp_recur(base, power):
    if power == 0:
        return 1
    else:
        return base * exp_recur(base, power - 1)
    
exponent = exp_recur(5, 4)

print(exponent)