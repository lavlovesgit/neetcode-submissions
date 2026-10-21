class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]* len(nums)
        def robs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=max(robs(i+1),nums[i]+robs(i+2))



            return memo[i]
        return robs(0)

        

        