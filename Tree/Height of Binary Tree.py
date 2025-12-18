'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        # code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1+ max(self.height(root.left),self.height(root.right))