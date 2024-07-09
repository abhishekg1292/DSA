# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:17:55 2024

@author: Abhishek Gupta
"""

class _Node:
    def __init__(self, element, nextElement):
        self._element = element
        self._next = nextElement
    
class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def enQueue(self, e):
        n = _Node(e, None)
        if self._front is None:
            self._front = n
        else:
            self._rear._next = n
        self._rear = n
        self._size = self._size+1
    
    def deQueue(self):
        if self.isEmpty():
            return None
        e = self._front._element
        self._front = self._front._next
        self._size = self._size-1
        if self.isEmpty():
            self._rear = None
        return e
    
    def first(self):
        if self.isEmpty():
            return None
        return self._front._element
    
    def last(self):
        if self.isEmpty():
            return None
        return self._rear._element
    
    def display(self):
        n = self._front
        while n:
            if n._next:
                print(n._element, '-->')
            else:
                print(n._element)
            n = n._next

Q = Queue()
Q.enQueue(5)
Q.enQueue(3)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
ele = Q.deQueue()
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('Is Queue Empty:',Q.isEmpty())
Q.enQueue(7)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
Q.enQueue(12)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
ele = Q.deQueue()
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('First Element:',Q.first())
        