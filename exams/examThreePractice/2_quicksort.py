"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    Got close to the right answer I messed up the base case

    the base case is:
    if i - j <= 1: return L
"""


"""
Write a function quicksort(L, i, j) that sorts the sublist L[i:j] using the quick sort algorithm. You must use the provided partition function.
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


def quicksort(L,i,j):
    #Base Case
    if j -i <= 1: return L

    #Divide
    pivot = partition(L, i, j)

    #Conquer
    quicksort(L,i,pivot)
    quicksort(L,pivot+1,j)

    #Combine
    return L



L1 = [5,4,3,2,1]

quicksort(L1,0,len(L1))

print(L1)

