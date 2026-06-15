class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=0
        res=0
        hm={0:1}
        for num in nums:
            pre=pre+num
            if(pre-k in hm):
                
                res=res+hm[pre-k]
            if pre not in hm:
                hm[pre]=1
            else:
                hm[pre]=hm[pre]+1
            
        return res

        