# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:20:55 2024

@author: Lenovo
"""

class QueueArray:
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data)==0
    
    def enQueue(self, e):
        self._data.append(e)
    
    def deQueue(self):
        if self.isEmpty():
            return None
        return self._data.pop(0)
    
    def first(self):
        if self.isEmpty():
            return None
        return self._data[0]
    
    def display(self):
        print(self._data)

Q = QueueArray()
Q.enQueue(5)
Q.enQueue(3)
Q.display()
print('Queue Length:', len(Q))
ele = Q.deQueue()
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('Is Queue Empty:',Q.isEmpty())
Q.enQueue(7)
Q.display()
print('Queue Length:', len(Q))
Q.enQueue(12)
Q.display()
print('Queue Length:', len(Q))
ele = Q.deQueue()
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('First Element:',Q.first())