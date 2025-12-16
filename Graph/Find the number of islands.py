class Solution:
    def numIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        
        visited =[[False]*m for _ in range(n)]
        
        directions=[
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
            ]
        def dfs(r,c):
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m :
                    if not visited[nr][nc] and grid[nr][nc] == 'L':
                        dfs(nr, nc)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    count += 1
                    dfs(i,j)
        return count
                    