import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        res=[]
        for i in nums:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        val=math.floor(len(nums)/3)
        for i in hm:
            if hm[i]>val:
                res.append(i)
        return res

        