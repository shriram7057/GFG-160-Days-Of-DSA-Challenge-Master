class Solution:
    def buildTree(self,inorder,preorder):
        idx={v:i for i,v in enumerate(inorder)}
        self.pre_i=0
        
        def solve(l,r):
            if l > r:
                return None
            root_val=preorder[self.pre_i]
            self.pre_i += 1
            root=Node(root_val)
            mid=idx[root_val]
            root.left=solve(l,mid-1)
            root.right=solve(mid+1,r)
            return root
        return solve(0,len(inorder)- 1)
            