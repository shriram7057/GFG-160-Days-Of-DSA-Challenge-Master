'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        # code here
        self.ans=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            
            self.ans = max(self.ans, node.data + left + right)
            
            return node.data + max(left,right)
            
        dfs(root)
        return self.ans