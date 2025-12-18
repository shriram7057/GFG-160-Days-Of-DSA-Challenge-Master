'''
# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        # code here
        self.ans=0
        def dfs(node):
            if not node:
                return -1
            lh=dfs(node.left)
            rh=dfs(node.right)
            self.ans=max(self.ans,lh+rh+2)
            return 1 + max(lh,rh)
            
        dfs(root)
        return self.ans
                    