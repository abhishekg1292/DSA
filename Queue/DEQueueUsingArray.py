# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:09:55 2024

@author: Lenovo
"""

class DoubleEndedQueueUsingArray:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data)==0
    
    def addFirst(self, e):
        self._data.insert(0, e)
    
    def addLast(self, e):
        self._data.append(e)
    
    def removeFirst(self):
        if self.isEmpty():
            return None
        return self._data.pop(0)
    
    def removeLast(self):
        if self.isEmpty():
            return None
        return self._data.pop()
    
    def first(self):
        if self.isEmpty():
            return None
        return self._data[0]
    
    def last(self):
        if self.isEmpty():
            return None
        return self._data[-1]
    
    def display(self):
        print(self._data)

D = DoubleEndedQueueUsingArray()
D.addFirst(5)
D.addFirst(3)
D.addLast(7)
D.addLast(12)
D.display()
print('Length:',len(D))
print(D.removeFirst())
print(D.removeLast())
D.display()
print('First Element:',D.first())
print('Last Element:',D.last())