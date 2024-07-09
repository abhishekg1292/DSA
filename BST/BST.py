# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:16:30 2024

@author: Lenovo
"""

class Node:    
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root
    
    def insert(self, e):
        if self._root is None:
            self._root = Node(e)
        else:
            currNode = None
            parent = self._root
            while parent:
                currNode = parent
                if e == parent._element:
                    return
                elif e < parent._element:
                    parent = parent._left
                else:
                    parent = parent._right
            
            if e < currNode._element:
                currNode._left = Node(e)
            else:
                currNode._right = Node(e)
    
    def delete(self, e):
        if self._root is None:
            return False
        
        currNode = self._root
        parent = None
        
        while currNode:
            if e < currNode._element:
                parent = currNode
                currNode = currNode._left
            elif e > currNode._element:
                parent = currNode
                currNode = currNode._right
            else:
                break
        
        if currNode is None:
            return False
        
        if (currNode._left is None) and (currNode._right is None):
            if currNode == self._root:
                self._root = None
            elif parent._left == currNode:
                parent._left = None
            else:
                parent._right = None
        elif (currNode._left is None) and (currNode._right is not None):
            if currNode == self._root:
                self._root = currNode._right
            elif parent._left == currNode:
                parent._left = currNode._right
            else:
                parent._right = currNode._right
        elif (currNode._left is not None) and (currNode._right is None):
            if currNode == self._root:
                self._root = currNode._left
            elif parent._left == currNode:
                parent._left = currNode._left
            else:
                parent._right = currNode._left
        else:
            lNode = currNode._left
            lNodeParent = currNode
            while lNode._right:
                lNodeParent = lNode
                lNode = lNode._right
            
            currNode._element = lNode._element
            
            if lNodeParent._left == lNode:
                lNodeParent._left = lNode._left
            else:
                lNodeParent._right = lNode._left
        return True
    
    def search(self, key):
        if self._root is None:
            return False
        
        parent = self._root
        
        while parent:
            if parent._element == key:
                return True
            elif key < parent._element:
                parent = parent._left
            else:
                parent = parent._right
        
        return False
    
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element)
            self.inorder(root._right)

B = BinarySearchTree()
B.insert(50)
B.insert(30)
B.insert(80)
B.insert(10)
B.insert(40)
B.insert(60)
B.insert(90)
B.inorder(B._root)
B.delete(50)
print()
B.inorder(B._root)
print(B.search(60))
print(B.search(66))

            
            
        
        
        