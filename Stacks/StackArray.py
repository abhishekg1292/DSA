# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:10:37 2024

@author: Abhishek Gupta
"""

class Stack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def pop(self):
        if self.isEmpty():
            return None
        
        return self._data.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        
        return self._data[-1]
    
    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:     
            print(self._data)

S = Stack()
S.push(5)
S.push(3)
S.display()
print(len(S))
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