import math
def timereq(piles:List[int],rate:int):
    s=0
    for i in piles:
        s+=math.ceil(i/rate)
    return s
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)

        while(l<=r):
            mid=(l+r)//2
            if (timereq(piles,mid)>h):
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans

    