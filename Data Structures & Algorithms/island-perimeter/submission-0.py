class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()

        rows=len(grid)
        cols=len(grid[0])
        def rec(i,j):
            if i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perim= rec(i, j + 1) + rec(i + 1, j) + rec(i, j - 1) + rec(i - 1, j)
            return perim
            
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return rec(i,j)
        return 0
        