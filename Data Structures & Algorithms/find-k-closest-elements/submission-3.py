class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L=0
        dist=[]
        for i in arr:
            d=abs(x-i)
            dist.append(d)
        s=0
        mins=float('inf')
        minarr=[]
        for R in range(len(dist)):
            s+=dist[R]
            if(R-L+1>k):
                s-=dist[L]
                L+=1
            if(R-L+1==k):
                if s < mins:
                    mins = s
                    minarr = arr[L:R+1]
                

            
        return minarr






        