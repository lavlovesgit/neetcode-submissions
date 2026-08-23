import math
class Solution:
    def timereq(self,piles:List[int],rate:int )->int :
        s=0
        for i in piles:
            s+=math.ceil(i/rate)

        return s


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p=max(piles)
        l,r=1,max(piles)
        while(l<=r):
            mid=(l+r)//2
            if (self.timereq(piles,mid)>h):
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans
        



        