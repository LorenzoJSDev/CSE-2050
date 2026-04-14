"""
Author: Lorenzo .S
Date: 4/11/2026

Notes:
    None
"""

def naive_quicksort(L):
    #Base Case
    if len(L) <= 1:
        return L

    #Divide
    pivot = L[-1]
    less = []
    eqaul = []
    greater = []
    for i in L:
        if i < pivot:
            less.apprend(i)
        elif i == pivot:
            eqaul.append(i)
        else:
            greater.append(i)

    #Conquer
    A = naive_quicksort(less)
    B = naive_quicksort(greater)

    #Combine
    sorted_list = A + eqaul + B
    return A + eqaul + B


L1 = [5,4,3,2,1]

print(naive_quicksort(L1))

