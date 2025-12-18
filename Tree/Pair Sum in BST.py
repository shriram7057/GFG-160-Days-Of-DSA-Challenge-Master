'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def findTarget(self, root, target): 
        # your code here.
        arr=[]
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)
            
        inorder(root)
        
        i,j=0,len(arr)-1
        while i<j:
            
            a=arr[i]+arr[j]
            if a==target:
                return True
            if a < target:
                i += 1
            else:
                j -= 1
        return False