'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isBST(self, root):
        #code here
        def check(node,low,high):
            if not node:
                return True
            if not (low<node.data<high):
                return False
            return check(node.left,low,node.data) and check(node.right,node.data,high)
        return check(root, float('-inf'),float('inf'))