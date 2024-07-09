# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:33:08 2024

@author: Abhishek Gupta
"""

def countSort(A):
    maxNum = max(A)
    temp = [0 for _ in range(maxNum+1)]
    
    for i in range(len(A)):
        temp[A[i]] = temp[A[i]]+1
    
    A = []
    for i in range(len(temp)):
        for j in range(temp[i]):
            A.append(i)
    return A

A = [3, 5, 8, 9, 6, 2, 3, 5, 5, 0, 0]
print('Original Array:',A)
A = countSort(A)
print('Sorted Array:',A)