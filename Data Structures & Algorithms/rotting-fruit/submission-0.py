class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=collections.deque()
        fresh=0
        print(q)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        minutes=0
        while q and fresh>0:
            for _ in range(len(q)):
                i,j=q.popleft()
                for di,dj in dir:
                    ni=i+di
                    nj=j+dj
                    if ni<0 or nj<0 or nj>=cols or ni>=rows:
                        continue
                        
                    if grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fresh-=1
                        q.append([ni,nj])
            minutes+=1
            
        if fresh>0 :
            return -1
        return minutes

        
                
