
def works(weights,maxdays,capacity):
    # arr,4,6
    cur_weight=0
    c=1
    
    for i in weights:
        if(cur_weight+i<=capacity):
            cur_weight+=i

        else:
            if(i<=capacity):
                cur_weight=i
                c+=1
            else:
                return False
    if(c<=maxdays):
        return True
    else:
        return False    
    

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        new=sorted(weights)
        l, r = max(weights), sum(weights)
        while(l<=r):
            mid=(l+r)//2
            if (not works(weights,days,mid)):
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans
        