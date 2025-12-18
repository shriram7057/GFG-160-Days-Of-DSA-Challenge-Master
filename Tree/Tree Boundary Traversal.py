'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        if not root:
            return []
        res=[root.data]
        
        def isLeaf(node):
            return node.left is None and node.right is None
        def leftBoundary(node):
            curr=node
            while curr:
                if not isLeaf(curr):
                    res.append(curr.data)
                if curr.left:
                    curr=curr.left
                else:
                    curr=curr.right
        def rightBoundary(node):
            curr=node
            temp=[]
            while curr:
                if not isLeaf(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr=curr.right
                else:
                    curr=curr.left
            for x in reversed(temp):
                res.append(x)
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)
            
        if root.left:
            leftBoundary(root.left)
        addLeaves(root.left)
        addLeaves(root.right)
        
        if root.right:
            rightBoundary(root.right)
        return res
