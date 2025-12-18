'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):
        #code here
        from collections import deque
        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            npde=q.popleft()
            if npde:
                res.append(npde.data)
                q.append(npde.left)
                q.append(npde.right)
            else:
                res.append(0)
        return res
        
    def deSerialize(self, arr):
        #code here
        from collections import deque
        if not arr:
            return None
        root=Node(arr[0])
        q=deque([root])
        i=1
        n=len(arr)
        
        while q and i<n:
            node=q.popleft()
            
            if arr[i]!=0:
                node.left=Node(arr[i])
                q.append(node.left)
            i+=1
            if i>=n:
                break
            if arr[i]!=0:
                node.right=Node(arr[i])
                q.append(node.right)
            i+=1
        return root
