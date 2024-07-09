# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:07:28 2024

@author: Lenovo
"""

def shellSort(A):
    n = len(A)
    gap = int(n/2)
    
    while gap >= 1:
        i = 0
        j = gap
        while (j<=n-1):
            if A[i]<=A[j]:
                i = i+1
                j = j+1
            else:
                k = j
                while k>=gap:
                    if A[k] >= A[k-gap]:
                        break
                    else:
                        A[k], A[k-gap] = A[k-gap], A[k]
                        k = k-gap
                i = i+1
                j = j+1
        gap = int(gap/2)

A = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
print('Original Array:',A)
shellSort(A)
print('Sorted Array:',A)