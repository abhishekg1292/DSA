# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:11:17 2024

@author: Lenovo
"""

class _Node:
    def __init__(self, e, nextElement):
        self._element = e
        self._next = nextElement

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, e):
        n = _Node(e, None)
        if self.isEmpty():
            self._top = n
            self._size = 1
            return
        
        n._next = self._top
        self._top = n
        self._size = self._size+1
    
    def pop(self):
        if self.isEmpty():
            return None
        
        e = self._top._element
        self._top = self._top._next
        self._size = self._size-1
        return e
    
    def top(self):
        if self.isEmpty():
            return None
        return self._top._element
    
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            n = self._top
            string = ""
            while n:
                if n._next:
                    string = string + str(n._element) + "-->"
                else:
                    string = string + str(n._element)
                n = n._next
            print(string)
        
S = Stack()
S.push(5)
S.push(3)
print(len(S))
S.display()
print(S.pop())
print(S.isEmpty())

print(S.pop())
print(S.isEmpty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
S.push(8)
print(S.pop())
        
            