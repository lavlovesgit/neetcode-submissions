class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        res=[-1,-1]
        while(l<=r):
                    mid=(l+r)//2
                    if(target<=nums[mid]):
                        if(target==nums[mid]):
                            res[0]=mid
                        r=mid-1
                        
                    if(target>nums[mid]):
                        l=mid+1
        l=0
        r=len(nums)-1
        while(l<=r):
                    mid=(l+r)//2
                    if(target<nums[mid]):
                        r=mid-1
                        
                    if(target>=nums[mid]):
                        if(target==nums[mid]):
                            res[1]=mid
                        l=mid+1
        return res

        