class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        q=collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
        dir=[[-1,0],[1,0],[0,1],[0,-1]]
        cur_distance=0
        while(q):
            i,j=q.popleft()
            
            for idelta,jdelta in dir:
                ni=i+idelta
                nj=j+jdelta
                if ni<0 or nj<0 or ni>=rows or nj>=cols:
                    continue
                if grid[ni][nj] == 2**31-1:
                    grid[ni][nj]=grid[i][j]+1
                    q.append([ni,nj])
                    


        