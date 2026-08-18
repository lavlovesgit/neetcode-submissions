class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

            if len(nums) == 1:
                return 0
            l=0
            r=len(nums)-1
            if nums[r] > nums[r-1] and r==len(nums)-1:
                return r

            while l<=r :
                mid=(l+r)//2
                if(mid <len(nums) and nums[mid+1]>nums[mid] ):
                    l=mid+1
                elif(mid>0 and nums[mid-1]>nums[mid]):
                    r=mid-1
                else:
                    return mid
                
            