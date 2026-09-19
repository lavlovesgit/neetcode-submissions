class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir=[[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]=='0':
                return
            grid[i][j]='0'
            for deltai,deltaj in dir:
                dfs(i+deltai,j+deltaj)
        c=0
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    c+=1
                    dfs(i,j)
        return c
        