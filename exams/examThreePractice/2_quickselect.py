"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    Had to RELOOK at the example code bcause I couldn't remember the algorithm
"""

"""
Write a function quickselect(L, i, j, k) 
that returns the k-th smallest element in the sublist L[i:j] 
using the quick select algorithm. You must use the provided partition function.
"""

def partition(L, i, j):
    pivot = j -1
    j = pivot -1
    #Pivot all items between left and right
    while i < j :
        while L[i] < L[pivot]:
            i = i + 1
        while i<j and L[j] >= L[pivot]:
            j = j - 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    #Swap pivot and i
    if L[i]>= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

def quickselect(L,i,j,k):
    #Divide
    pivot = partition(L,i,j)

    #BaseCase
    if k == pivot+1:
        return L[pivot]
    #Conquer
    elif k <=pivot:
        return quickselect(L,i,pivot,k)
    else:
        return quickselect(L,pivot+1,j,k)


