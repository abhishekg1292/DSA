# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:18:11 2024

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
            if e < root._element:
                root._left = self.recInsert(root._left, e)
            elif e > root._element:
                root._right = self.recInsert(root._right, e)
        else:
            n = _Node(e)
            root = n
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end = " ")
            self.inorder(root._right)

B = BinarySearchTree()
B._root = B.recInsert(B._root, 50)
B.recInsert(B._root, 30)
B.recInsert(B._root, 80)
B.recInsert(B._root, 10)
B.recInsert(B._root, 40)
B.recInsert(B._root, 60)
B.recInsert(B._root, 90)
B.recInsert(B._root, 90)
B.inorder(B._root)