# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:08:25 2024

@author: Lenovo
"""

class _Node:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self, root=None):
        self._root = root
    
    def genTree(self, e, leftTree, rightTree):
        self._root = _Node(e, leftTree._root, rightTree._root)
    
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end=" ")
            self.inorder(root._right)
    
    def preorder(self, root):
        if root:
            print(root._element, end=" ")
            self.preorder(root._left)
            self.preorder(root._right)
    
    def postorder(self, root):
        if root:
            self.postorder(root._left)
            self.postorder(root._right)
            print(root._element, end=" ")
    
    def countNodes(self, root):
        if root is None:
            return 0
        
        leftCount = self.countNodes(root._left)
        rightCount = self.countNodes(root._right)
        return leftCount + rightCount + 1
    
    def height(self, root):
        if root is None:
            return 0
        leftHeight = self.height(root._left)
        rightHeight = self.height(root._right)
        
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1
        

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
x.genTree(40,a,a)
y.genTree(60,a,a)
z.genTree(20,x,a)
r.genTree(50,a,y)
s.genTree(30,r,a)
t.genTree(10,z,s)
print('Inorder Traversal')
t.inorder(t._root)
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print("Node Count: ", t.countNodes(t._root))
print("Tree Height: ", t.height(t._root))
