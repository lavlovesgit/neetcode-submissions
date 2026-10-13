class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        minc=float('inf')
        
        for r in range(len(nums)):
            s=s+nums[r]
            while s>=target:
                minc=min(minc,r-l+1)
                s-=nums[l]
                l+=1
                
                
            
        return 0 if minc == float('inf') else minc
        
            

        