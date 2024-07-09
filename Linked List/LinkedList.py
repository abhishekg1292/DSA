# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 08:27:29 2024

@author: Lenovo
"""

class _Node:
    def __init__(self, e, nextElement):
        self._element = e
        self._next = nextElement
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def addLast(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._size = self._size + 1
            return
        
        self._tail._next = n
        self._tail = n
        self._size = self._size + 1
    
    def addFirst(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._size = self._size + 1
            return
        
        n._next = self._head
        self._head = n
        self._size = self._size + 1
    
    def addAny(self, e, pos):
        if pos == 0:
            self.addFirst(e)
            return
        
        if pos == -1:
            self.addLast(e)
            return
        
        if (pos < self._size) and (pos>0):
            n = _Node(e, None)
            p = self._head
            for i in range(0, pos-1):
                p = p._next
            n._next = p._next
            p._next = n
            self._size = self._size + 1
            return
    
    def removeFirst(self):
        if self.isEmpty():
            print("Empty Linked List")
            return
        
        e = self._head._element
        self._head = self._head._next
        self._size = self._size - 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e
    
    def removeLast(self):
        if self.isEmpty():
            print("Empty Linked List")
            return
        
        if self._size == 1:
            e = self._tail._element
            self._head = None
            self._tail = None
            self._size = 0
            return e
        
        pp = self._head
        p = pp._next
        
        while p._next:
            pp = p
            p = pp._next
        
        e = p._element
        pp._next = None
        self._tail = pp
        self._size = self._size - 1
        return e     
    
    def removeAny(self, pos):
        if self.isEmpty():
            print("Empty Linked List")
            return -1
        
        if pos == 0:
            return self.removeFirst()
        
        if (pos == -1) or (pos == self._size-1):
            return self.removeLast()
        
        if (pos > 0) and (pos < self._size):
            i = 1
            pp = self._head
            p = pp._next
            while i < pos:
                pp = p
                p = pp._next
                i = i+1
            e = p._element
            pp._next = p._next
            self._size = self._size-1
            return e
        else:
            return -1            
        
        
    def display(self):
        if self.isEmpty():
            print("Empty Linked List")
        else:
            p = self._head
            string = ''
            while p:
                if p._next:
                    string = string + str(p._element) + '-->'
                else:
                    string = string + str(p._element)
                p = p._next
            print(string)
    
    def search(self, key):
        if self.isEmpty():
            return -1
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            index = index + 1
            p = p._next
        return -1
                
            
L = LinkedList()
L.addLast(7)
L.addLast(4)
L.addLast(12)
L.addLast(8)
L.addLast(3)
L.display()
print('Size:',len(L))
L.addAny(20,3)
L.display()
print('Size:',len(L))
L.addAny(40,5)
L.display()
print('Size:',len(L))
L.addAny(42,-1)
L.display()
print(L.search(42))
print(L.search(20))
print("Removed First: ", L.removeFirst())
L.display()
print("Removed Last: ", L.removeLast())
L.display()     
print("Removed at 2nd position: ", L.removeAny(2))
L.display()    