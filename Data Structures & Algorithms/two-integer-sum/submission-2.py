class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        res=[]
        for i in range(len(nums)):
            hm[nums[i]]=i

        
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hm and hm[comp]!=i:
                res.append(i)
                res.append(hm[comp])
                break
        return res


