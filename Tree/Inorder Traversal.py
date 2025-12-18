'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        # code here
        res=[]
        def dfs(node):
            if not Node:
                return
            dfs(node.left)
            res.append(node.data)
            dfs(node.right)
        dfs(root)
        return res