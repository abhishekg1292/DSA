# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:08:56 2024

@author: Abhishek Gupta
"""

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while (j>=0) and (A[j]>key):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

if __name__ == '__main__':
    A = [54, 78, 64, 92, 34, 86, 28, 28]
    insertion_sort(A)
    print(A)