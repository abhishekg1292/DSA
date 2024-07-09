# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:00:42 2024

@author: Lenovo
"""

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        key = A[i]
        while j >= 0:
            if key >= A[j]:
                break
            else:
                A[j+1] = A[j]
                j = j - 1
        A[j+1] = key

A = [3,5,8,9,6,2]
print('Original Array:',A)
insertionSort(A)
print('Sorted Array:',A)