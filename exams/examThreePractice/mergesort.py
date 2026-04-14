"""
Author: Lorenzo .S
Date: 4/11/2026


Notes: Need to remeber how to write the merge function.
"""

def merge(A,B,L):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    L[i+j:] = A[i:] + B[j:] #Forgot to put the colon after L[i+j

def mergesort(L):

    #Base Case
    if len(L) == 1:
        return

    #Divide
    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]

    #Conquer
    mergesort(A)
    mergesort(B)

    #Combine
    merge(A,B,L)


list = [9,5,1,2,3,4]

print(list)

mergesort(list)

print(list)