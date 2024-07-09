# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:19:39 2024

@author: Abhishek Gupta
"""

def binarySearchIterative(A, key):
    start = 0
    end = len(A)-1
    
    while start <= end:
        mid = (start+end)//2
        
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

def binarySearchRecursive(A, key, l, r):
    if l > r:
        return -1
    
    mid = (l+r)//2
    if A[mid] == key:
        return mid
    elif key < A[mid]:
        r = mid-1
    else:
        l = mid+1
    return binarySearchRecursive(A, key, l, r)
    

A = [15,21,47,84,96]
found = binarySearchIterative(A,84)
print('Result: ',found)

found = binarySearchRecursive(A,84,0,len(A)-1)
print('Result: ',found)