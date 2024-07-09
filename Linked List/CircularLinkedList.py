# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:56:01 2024

@author: Lenovo
"""

class _Node:
    def __init__(self, e, nextElement):
        self._element = e
        self._next = nextElement

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size==0
    
    def addLast(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._tail._next = n
            self._size = 1
        else:
            self._tail._next = n
            n._next = self._head
            self._tail = n
            self._size = self._size+1
    
    def addFirst(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._head = n
            self._tail = n
            self._tail._next = n
            self._size = 1
        else:
            self._tail._next = n
            n._next = self._head
            self._head = n
            self._size = self._size + 1
    
    def addAny(self, e, pos):
        if pos == 0:
            self.addFirst(e)
        elif (pos == -1) or (pos == self._size - 1):
            self.addLast(e)
        elif (pos > 0) and pos < (self._size):
            pp = self._head
            p = pp._next
            for i in range(1, pos):
                pp = p
                p = pp._next
            n = _Node(e, None)
            pp._next = n
            n._next = p
            self._size = self._size + 1
        else:
            raise IndexError("Input valid list index")
    
    def removeFirst(self):
        if self.isEmpty():
            return -1
        e = self._head._element
        self._head = self._head._next
        self._tail._next = self._head
        self._size = self._size - 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e
        
    def removeLast(self):
        if self.isEmpty():
            return -1
        e = self._tail._element
        pp = self._head
        p = pp._next
        while p._next != self._head:
            pp = p
            p = pp._next
        pp._next = self._head
        self._tail = pp
        self._size = self._size - 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e
    
    def removeAny(self, pos):
        if pos == 0:
            return self.removeFirst()
        elif (pos == -1) or (pos == self._size-1):
            return self.removeLast()
        elif (pos>0) and (pos<self._size):
            pp = self._head
            p = pp._next
            for i in range(1, pos):
                pp = p
                p = pp._next
            e = p._element
            pp._next = p._next
            self._size = self._size-1
            return e
        else:
            raise IndexError("Index Not Found")
            
    def display(self):
        p = self._head
        string = ""
        while 1:
            if p._next == self._head:
                string = string + str(p._element)
                break
            else:
                string = string + str(p._element) + "-->"
            p = p._next
        print(string)
    
    def search(self, key):
        p = self._head
        index = 0
        while 1:
            if p._element == key:
                return index
            p = p._next
            index = index + 1
            if p == self._head:
                break
        return -1

C = CircularLinkedList()
C.addLast(7)
C.addLast(4)
C.addLast(12)
C.addLast(8)
C.addLast(3)
C.display()
print('Size:',len(C))
C.addAny(25,3)
C.display()
print('Size:',len(C))
C.addAny(22,0)
C.display()
print('Size:',len(C))
print('Search Key 12:',C.search(12))
print('Search Key 92:',C.search(92))
print("Remove Last: ", C.removeLast())
C.display()
print("Remove First: ", C.removeFirst())
C.display()
print("Remove at 3rd position: ", C.removeAny(3))
C.display()
print('Size:',len(C))
print("Remove at 10th position: ", C.removeAny(10))
C.display()