
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	n=len(mat)
    	m=len(mat[0])
    	
    	for i in range(n):
    	    if mat[i][0]<=x <=mat[i][m-1]:
    	        l,r=0,m-1
    	        while l<=r:
    	            mid=(l+r)>>1
    	            if mat[i][mid]==x:
    	                return True
    	            elif mat[i][mid]<x:
    	                l=mid+1
    	            else:
    	                r=mid-1
        return False
