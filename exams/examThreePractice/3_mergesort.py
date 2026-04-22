"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    Perfect!
"""

"""
Write a function mergesort(L) that 
sorts a list L using the merge sort algorithm. 
You must use the provided merge function.
"""

def merge(A,B,L):
    """ Merge two sorted lists"""
    i , j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i = i +1
        else:
            L[i+j] = B[j]
            j = j +1
    L[i+j:]  = A[i:] + B[j:]

def mergesort(L):
    #Base Case
    if len(L) == 1: return L

    #Divide
    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]

    #Conquer
    mergesort(A)
    mergesort(B)

    #Combine
    merge(A,B,L)


L1=[5,4,3,2,1]

mergesort(L1)

print(L1)