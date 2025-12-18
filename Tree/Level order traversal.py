"""
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
"""

class Solution:
    def levelOrder(self, root):
        # code here
        if not root:
            return []
        from collections import deque
        q=deque([root])
        res=[]
        while q:
            size=len(q)
            level = []
            for _ in range(size):
                node=q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res