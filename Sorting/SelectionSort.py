# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:19:28 2024

@author: Lenovo
"""

def selectionSort(A):
    if len(A) <= 1:
        return A
    
    minElement = min(A)
    minIdx = A.index(minElement)
    temp = A[0]
    A[0] = minElement    
    A[minIdx] = temp
    
    A[1:] = selectionSort(A[1:])
    return A

A = [64, 25, 12, 22, 11]
print("Original array: ", A)
print("Sorted array:", selectionSort(A))     
        