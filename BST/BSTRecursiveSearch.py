# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:22:43 2024

@author: Lenovo
"""

class _Node:
    def __init__(self, e, left=None, right=None):
        self._element = e
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root
    
    def recInsert(self, root, e):
        if root:
            if root._element < e:
                root._right = self.recInsert(root._right, e)
            elif root._element > e:
                root._left = self.recInsert(root._left, e)
        else:
            root = _Node(e)
        return root
    
    def recSearch(self, root, e):
        if root:
            if e < root._element:
                return self.recSearch(root._left, e)
            elif e > root._element:
                return self.recSearch(root._right, e)
            else:
                return True
        else:
            return False
    
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end = ' ')
            self.inorder(root._right)

B = BinarySearchTree()
B._root = B.recInsert(B._root,50)
B.recInsert(B._root,30)
B.recInsert(B._root,80)
B.recInsert(B._root,10)
B.recInsert(B._root,40)
B.recInsert(B._root,60)
B.recInsert(B._root,90)
B.inorder(B._root)
print()
print(B.recSearch(B._root,60))
print(B.recSearch(B._root,30))
print(B.recSearch(B._root,70))