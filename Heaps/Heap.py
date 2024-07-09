# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:23:54 2024

@author: Lenovo
"""

class Heap:
    def __init__(self, maxSize=10):
        self._maxSize = maxSize
        self._list = [-1 for _ in range(maxSize+1)]
        self._currentSize = 0
    
    def __len__(self):
        return self.__currentSize
    
    def isEmpty(self):
        return self._currentSize == 0
    
    def insert(self, e):
        if self._currentSize == self._maxSize:
            raise Exception("Heap is Full")
        else:
            self._currentSize = self._currentSize + 1
            initialIdx = self._currentSize
            
            while initialIdx > 1:
                if e > self._list[initialIdx//2]:
                    self._list[initialIdx] = self._list[initialIdx//2]
                    initialIdx = initialIdx//2
                else:
                    break
            self._list[initialIdx] = e
    
    def _max(self):
        if self._currentSize == 0:
            return None
        return self._list[1]
    
    def deleteMax(self):
        if self.isEmpty():
            print("Heap is empty")
            return
        maxElement = self._list[1]
        self._list[1] = self._list[self._currentSize]
        self._list[self._currentSize] = -1
        self._currentSize = self._currentSize - 1
        
        i = 1
        j = 2*i
        while j<=self._currentSize:
            if (j<self._currentSize) and (self._list[j] < self._list[j+1]):
                j = j+1
            
            if self._list[i] < self._list[j]:
                temp = self._list[i]
                self._list[i] = self._list[j]
                self._list[j] = temp
                i = j
                j = 2*i
            else:
                break
            
        return maxElement

def HeapSort(A):
    H = Heap()
    
    for i in range(len(A)):
        H.insert(A[i])
    
    A = []
    
    while not H.isEmpty():
        A.append(H.deleteMax())
    return A

S = Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
print(S._list)
S.insert(40)
print(S._list)
S.deleteMax()
print(S._list)

A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
A = HeapSort(A)
print('Sorted Array:',A)
                