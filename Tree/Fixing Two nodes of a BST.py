'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def correctBST(self, root):
    # your code here
        self.first=None
        self.middle=None
        self.last=None
        self.prev=None
    
        def inorder(node):
            if not node:
                return
            inorder(node.left)
        
            if self.prev and node.data < self.prev.data:
                if not self.first:
                    self.first=self.prev
                    self.middle=node
                else:
                    self.last=node
            self.prev=node
            inorder(node.right)
        inorder(root)
    
        if self.first and self.last:
            self.first.data,self.last.data,=self.last.data,self.first.data
        else:
            self.first.data,self.middle.data=self.middle.data,self.first.data
        