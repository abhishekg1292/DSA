# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:58:51 2024

@author: Lenovo
"""

from InsertionSort import insertion_sort

def bucket_sort(A):
    n = len(A)
    bucketList = [[] for _ in range(10)]
    
    minElement = min(A)
    maxElement = max(A)
    
    for i in range(n):
        idx = int(10*(A[i]-minElement)/(maxElement-minElement+1))
        bucketList[idx].append(A[i])
    
    A = []
    for i in range(10):
        insertion_sort(bucketList[i])
        A.extend(bucketList[i])
    return A
    
if __name__ == '__main__':
    A = [54, 78, 64, 92, 34, 86, 28, 28, 0.2]
    A = bucket_sort(A)
    print(A)
        