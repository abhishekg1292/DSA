# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:25:43 2024

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
    
    def addLast(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._front = n
        else:
            self._rear._next = n
        self._rear = n
        self._size = self._size+1
    
    def addFirst(self, e):
        if self.isEmpty():
            n = _Node(e, None) 
            self._front = n
            self._rear = n
        else:
            n = _Node(e, self._front)
            self._front = n
        self._size = self._size+1
    
    def removeFirst(self):
        if self.isEmpty():
            return None
        
        e = self._front._element
        self._front = self._front._next
        self._size = self._size-1
        if self.isEmpty():
            self._front = None
            self._rear = None
        return e
    
    def removeLast(self):
        if self.isEmpty():
            return None
        
        if self._size == 1:
            e = self._rear._element
            self._size = 0
            self._front = None
            self._rear = None
            return e
                
        p = self._front._next
        pp = self._front
        
        while p._next:
            pp = p
            p = p._next
        e = p._element
        pp._next = None
        self._rear = pp
        self._size = self._size-1
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
        if self.isEmpty():
            print("Empty Queue")
        else:
            string = ''
            n = self._front
            while n:
                if n._next:
                    string = string + str(n._element) + "-->"
                else:
                    string = string + str(n._element)
                n = n._next
            print(string)

D = Queue()
D.addFirst(5)
D.addFirst(3)
D.addLast(7)
D.addLast(12)
D.display()
print('Length:',len(D))
print(D.removeFirst())
print(D.removeLast())
D.display()
print(D.first())
print(D.last())