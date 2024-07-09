# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:41:08 2024

@author: Lenovo
"""

class HashLinearProbing:
    def __init__(self, size):
        self._size = size
        self._list = [None for _ in range(size)]
    
    def hashFunction(self, key):
        return key % self._size
    
    def insert(self, element):
        indx = self.hashFunction(element)
        originalIndx = self.hashFunction(element)
        while (self._list[indx] is not None):
            indx = (indx+1)%(self._size)
            if indx == originalIndx:
                break
        
        if self._list[indx] is None:
            self._list[indx] = element
        else:
            raise Exception("Hash Table is Full")
    
    def search(self, element):
        indx = self.hashFunction(element)
        originalIndx = self.hashFunction(element)
        
        while (self._list[indx] != element):
            indx = (indx+1) % self._size
            
            if self._list[indx] == element:
                return indx            
            
            if indx == originalIndx:
                return None
        return indx
    
    def delete(self, element):
        indx = self.search(element)
        if indx is None:
            raise KeyError("Key not Found")
        else:
            self._list[indx] = None
            self.rehash()
    
    def rehash(self):
        originalList = [i for i in self._list[:] if i is not None]
        self._list = [None for _ in range(self._size)]
        
        for key in originalList:
            self.insert(key)
    
    def display(self):
        print(self._list)

HC = HashLinearProbing(12)
#HC.display()
HC.insert(54)
HC.insert(78)
HC.insert(64)
HC.insert(92)
HC.insert(34)
HC.insert(86)
HC.insert(28)
HC.display()
print(HC.search(34))
print(HC.search(78))
HC.delete(54)
print(HC.search(78))
        