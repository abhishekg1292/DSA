# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:22:02 2024

@author: Lenovo
"""

def linearSearch(A, key):
    index = 0
    while index<=len(A)-1:
        if A[index]==key:
            return index
        index+=1
    return -1

A = [84, 21, 47, 96, 15]
found = linearSearch(A,96)
print('Result:',found)