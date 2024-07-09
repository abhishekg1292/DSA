# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 09:53:32 2024

@author: Abhishek Gupta
"""

class _Node:
    def __init__(self, element, nextElement, prevElement):
        self._element = element
        self._next = nextElement
        self._prev = prevElement

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def addLast(self, e):
        n = _Node(e, None, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._size = 1
            return
        
        self._tail._next = n
        n._prev = self._tail
        self._tail = n
        self._size = self._size+1
    
    def addFirst(self, e):
        n = _Node(e, None, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._size = 1
            return
        
        n._next = self._head
        self._head._prev = n
        self._head = n
        self._size = self._size+1
    
    def addAny(self, e, pos):
        if pos == 0:
            self.addFirst(e)
            return
        
        if (pos == -1) or (pos == self._size-1):
            self.addLast(e)
            return
        
        if (pos > 0) and (pos < self._size):
            n = _Node(e, None, None)
            p = self._head
            for i in range(1, pos):
                p = p._next
            x = p._next
            p._next = n
            n._next = x
            n._prev = p
            x._prev = n
            self._size = self._size+1
        else:
            print("Position doesnt exist")
    
    def removeFirst(self):
        if self.isEmpty():
            return -1
        
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size = self._size - 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e
    
    def removeLast(self):
        if self.isEmpty():
            return -1
        
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size = self._size-1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e
    
    def removeAny(self, pos):
        if pos == 0:
            return self.removeFirst()
        if (pos == -1) or (pos == self._size - 1):
            return self.removeLast()
        if (pos > 0) and (pos < self._size):
            p = self._head
            for i in range(1, pos):
                p = p._next
            
            e = p._next._element
            p._next = p._next._next
            p._next._prev = p
            self._size = self._size - 1
            return e
        else:
            return -1
        
    
    def displayFwd(self):
        p = self._head
        string = ""
        while p:
            if p._next:
                string = string + str(p._element) + "-->"
            else:
                string = string + str(p._element)
            p=p._next
        print(string)
        
    def displayRev(self):
        p = self._tail
        string = ""
        while p:
            if p._prev:
                string = string + str(p._element) + "<--"
            else:
                string = string + str(p._element)
            p=p._prev
        print(string)
                
L = DoubleLinkedList()
L.addLast(7)
L.addLast(4)
L.addLast(12)
L.addLast(8)
L.addLast(3)
L.displayFwd()
print('Size:',len(L))
L.addAny(20,3)
L.displayFwd()
print('Size:',len(L))
L.displayRev()
print("Removing First Element: ", L.removeFirst())
L.displayFwd()
print("Removing Last Element: ", L.removeLast())
L.displayFwd()
print("Removing 2nd Element: ", L.removeAny(2))
L.displayFwd()