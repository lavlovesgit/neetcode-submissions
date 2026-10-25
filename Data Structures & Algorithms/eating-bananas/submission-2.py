import math
def eatinghours(rate,piles):
        h=0
        for i in piles:
            h+=math.ceil(i/rate)
        return h
class Solution:
    


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while(l<=r):
            mid=(l+r)//2
            if eatinghours(mid,piles)<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
            

        