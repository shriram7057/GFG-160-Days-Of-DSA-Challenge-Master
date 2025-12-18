'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        # code here
        stack=[]
        curr=root
        
        while True:
            while curr:
                stack.append(curr)
                curr=curr.left
            if not stack:
                return -1
                
            node=stack.pop()
            k -= 1
            if k == 0:
                return node.data
            curr=node.right