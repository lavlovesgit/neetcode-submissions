class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm=set(nums)
        longest=0

        for num in hm:
            if (num-1) not in hm:
                l=1
                while(num+l) in hm:
                    l+=1
                longest=max(l,longest)
        return longest


        
        
        
        
            
            
        