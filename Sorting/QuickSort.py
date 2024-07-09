# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:08:09 2024

@author: Abhishek Gupta
"""

def quickSort(A):
    if len(A) <= 1:
        return A
    
    pivot = A[0]
    leftArr = [x for x in A if x < pivot]
    midArr = [x for x in A if x == pivot]
    rightArr = [x for x in A if x > pivot]
    
    return quickSort(leftArr) + midArr + quickSort(rightArr)

# Example usage:
arr = [10, 7, 8, 9, 1, 5, 10, 3,4 ,3, 0]
sorted_arr = quickSort(arr)
print("Sorted array is:", sorted_arr)
