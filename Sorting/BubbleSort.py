# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:24:10 2024

@author: Lenovo
"""

def bubbleSort(A):
    startInd = 1
    passInd = 0
    lenReduction = 1
    while (startInd) or (passInd):
        passInd = 0
        startInd = 0
        for i in range(len(A)-lenReduction):
            if A[i+1]<A[i]:
                x = A[i+1]
                A[i+1] = A[i]
                A[i] = x
                passInd = 1
        lenReduction+=1

A = [50, 3, 5, 8, 9, 6, 2, 0.9, 8]
print('Original Array:',A)
bubbleSort(A)
print('Sorted Array:',A)