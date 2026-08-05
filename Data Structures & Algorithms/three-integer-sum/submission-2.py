class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        il=[]
        ol=[]
        seen={}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            target=-1*nums[i]
            
            x=i+1
            y=len(nums)-1
            while(x<y):
                s=nums[x]+nums[y]
                if(s<target):
                    x+=1
                elif (s>target):
                    y-=1
                else:
                    il = [-1*target, nums[x], nums[y]]
                    x+=1
                    y-=1
                    ol.append(il)
                    while x < y and nums[x] == nums[x-1]:
                        x += 1

                    while x < y and nums[y] == nums[y+1]:
                         y -= 1
        return ol
                    

            



        