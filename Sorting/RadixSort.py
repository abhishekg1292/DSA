# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:27:03 2024

@author: Abhishek Gupta
"""

def getPlace(num, n):
    return (num//pow(10, n-1))%10

def radixSort(A):
    maxNum = max(A)
    numDigits = len(str(maxNum))
    
    for i in range(numDigits):
        bins = [[] for _ in range(10)]
        for j in range(len(A)):
            e = getPlace(A[j], i+1)
            bins[e].append(A[j])
        
        A = []
        for j in range(10):
            A.extend(bins[j])
    return A

A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
A=radixSort(A)
print('Sorted Array:',A)
            