class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        def rec(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]=='0':
                return 
            grid[i][j]='0'
            for deltai,deltaj in dir:
                rec(i+deltai,j+deltaj)
            
        rows=len(grid)
        cols=len(grid[0])
        c=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    c+=1
                    rec(i,j)
        return c