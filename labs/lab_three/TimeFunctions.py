

""" Test several times and return minimum time"""

#=== Imports ===#

import time




#=== Functions ===#

def time_function(func,agrs,n_trials=10) -> float:

    minimum_run_time = float('inf')

    for i in range(n_trials): 
        start = time.time()
        func(agrs)
        end = time.time()
        elasped = end - start
        
        if minimum_run_time > elasped:
            minimum_run_time = elasped

    return minimum_run_time





#=== Script Entry Point ===#

if __name__ == '__main__':
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]

    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]

    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))

    print("t(L2) = {:.3g} ms".format(t2*1000))