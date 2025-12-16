class Solution:
	def floodFill(self, image, sr, sc, newColor):
		# code here
        rows = len(image)
        cols = len(image[0])
        
        original = image[sr][sc]
        
        if original == newColor:
            return image
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if image[r][c] != original:
                return 
            image[r][c]=newColor
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr,sc)
        return image
        