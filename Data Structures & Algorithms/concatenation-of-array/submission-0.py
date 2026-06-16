class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [None] * 2*len(nums) 
        for i in range(len(nums)):
            arr[i]=nums[i]

        for i in range(len(nums)):
            arr[i+len(nums)]=nums[i]
        return arr


        
        
        